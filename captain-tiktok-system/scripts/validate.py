#!/usr/bin/env python3
"""Read-only repository checks using only the Python standard library."""

import hashlib
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    'captain-tiktok', 'captain-tiktok-computer-prep',
    'captain-tiktok-device-reset', 'captain-tiktok-apple-id',
    'captain-tiktok-shadowrocket-treehole', 'captain-tiktok-ip-purchase',
    'captain-tiktok-ip-diagnostics', 'captain-tiktok-operations',
    'captain-tiktok-shop', 'captain-tiktok-governance',
}
ERRORS = []


def check(condition, message):
    if not condition:
        ERRORS.append(message)


def read(relative):
    path = ROOT / relative
    try:
        return path.read_text(encoding='utf-8')
    except (OSError, UnicodeError) as error:
        ERRORS.append(f'{relative}: {error}')
        return ''


def section(text, start, end):
    if start not in text or end not in text.split(start, 1)[1]:
        ERRORS.append(f'Missing section: {start}')
        return ''
    return text.split(start, 1)[1].split(end, 1)[0]


def main():
    actual = {p.name for p in ROOT.glob('captain-*') if p.is_dir()}
    check(actual == EXPECTED, 'Skill directory inventory changed')
    for name in sorted(EXPECTED):
        text = read(f'{name}/SKILL.md')
        front = re.match(r'\A---\n(.*?)\n---(?:\n|$)', text, re.S)
        check(front is not None, f'{name}: missing frontmatter')
        if front:
            check(f'name: {name}' in front.group(1).splitlines(),
                  f'{name}: name does not match folder')
            check(bool(re.search(r'^description: .+', front.group(1), re.M)),
                  f'{name}: missing description')

    for path in ROOT.glob('captain-*/**/*.md'):
        text = read(path.relative_to(ROOT))
        check('\ufffd' not in text, f'{path.name}: replacement character')
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            target = link.split('#', 1)[0]
            if target and '://' not in target:
                check((path.parent / target).is_file(),
                      f'{path.relative_to(ROOT)}: broken file link {link}')

    seen = set()
    for line in read('SHA256SUMS.txt').splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        if not match:
            ERRORS.append('Malformed checksum entry')
            continue
        digest, name = match.groups()
        target = (ROOT / name).resolve()
        if ROOT not in target.parents or not target.is_file():
            ERRORS.append(f'Invalid checksum path: {name}')
            continue
        check(name not in seen, f'Duplicate checksum: {name}')
        seen.add(name)
        check(hashlib.sha256(target.read_bytes()).hexdigest() == digest,
              f'Checksum mismatch: {name}')
    expected_files = {'VERSION'} | {
        str(f.relative_to(ROOT)).replace('\\', '/')
        for name in EXPECTED for f in (ROOT / name).rglob('*') if f.is_file()
    }
    check(seen == expected_files, 'Checksum inventory differs from Skill files')
    check(read('VERSION') == read('captain-tiktok/VERSION'), 'Version mismatch')

    entry = read('captain-tiktok/SKILL.md')
    prep = read('captain-tiktok-computer-prep/SKILL.md')
    sop = read('captain-tiktok-computer-prep/references/computer-prep.md')
    actions = re.findall(r'^\d+\. (.+)$',
                         section(entry, '## 准备动作清单', '## 第一阶段'), re.M)
    check(actions == ['准备手机', '下载爱思助手', '打开 Google', '下载 Chrome',
                      '安装 Chrome', '购买 Google 账号', '修改账号资料',
                      '登录 Google', '登录 NotebookLM', '核对准备结果'],
          'Opening action list changed')
    check(re.findall(r'^\| (P\d+) \|', prep, re.M) ==
          ['P01', 'P02', 'P16', 'P17', 'P18', 'P19', 'P20', 'P21', 'P22', 'P23'],
          'Preparation node order changed')
    refusal = '这个问题不在本次课前准备范围内，我不能在这里展开，请联系【船长电商】工作人员。'
    closing = '课前准备工作已完成，请调整好心态，准备开课，祝你学习顺利！'
    check(refusal in entry, 'Missing fixed refusal')
    check(closing in entry and closing in sop, 'Missing fixed completion text')
    check('结束后再问框架外问题仍固定拒答' in entry, 'Missing post-completion boundary')
    check('每条用户消息只处理一次，只作用于当前编号节点' in entry,
          'Missing single-step skip constraint')
    purchase = section(sop, '## P19：购买 Google 账号', '## P20')
    check(re.findall(r'https://[^\s]+', purchase) == [
        'https://gcnvra3kee7w.feishu.cn/wiki/Fr7ewDdMRi6Ga6kiD2ecropInA3?from=from_copylink'
    ], 'Purchase step must contain only the course tutorial URL')
    check('humkt' not in prep + sop, 'Legacy purchase site reintroduced')
    check('买好后回复：**Google 账号已购买**' in purchase, 'Missing purchase confirmation')

    for path in ROOT.rglob('*'):
        if '.git' in path.parts or not path.is_file():
            continue
        check(path.stat().st_size < 5 * 1024 * 1024,
              f'Unexpected large file: {path.relative_to(ROOT)}')
    if ERRORS:
        print('FAIL\n' + '\n'.join(ERRORS))
        return 1
    print(f'PASS: {len(EXPECTED)} Skills, {len(seen)} file hashes, local links and static flow checks')
    print('Static checks only; not a model-behavior or cross-platform installation test.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
