# Captain TikTok Skills

船长电商课前准备 Skill 系统。此目录可直接作为 GitHub 仓库根目录；无需上传历史压缩包、软件安装包或本机配置。

## 当前版本

2026-09-23 本地候选版，版本标识见 `VERSION`。核心执行规则以各模块的 `SKILL.md` 为准，本说明不替代规则。此包尚未发布为官方版本，也未覆盖本机已安装版本。

## 学员入口

使用 `captain-tiktok`，输入“开始使用”。开场展示动作清单，之后每次执行一步：

1. 准备手机
2. 下载爱思助手
3. 打开 Google
4. 下载 Chrome
5. 安装 Chrome
6. 购买 Google 账号
7. 修改账号资料
8. 登录 Google
9. 登录 NotebookLM
10. 核对准备结果

粉猫、树洞购买及订阅配置由 AI 对话前的课程准备安排，不再逐项重教。Google 访问只确认页面实际打开；账号购买只发既定飞书教程。

框架外问题固定拒答并转【船长电商】工作人员；当前动作解释和实际故障仍可处理。不因要求换篇、暂停或已结束而开放其他课程。验收成功只回复：

> 课前准备工作已完成，请调整好心态，准备开课，祝你学习顺利！

## 文件组织

每个 `captain-*` 文件夹都是一个 Skill，包含自己的 `SKILL.md`。详细资料放在对应 `references/`，展示元数据放在 `agents/`。仓库级校验工具位于 `scripts/`。

| 文件夹 | 职责 |
|---|---|
| captain-tiktok | 总入口、开场清单、范围和流程控制 |
| captain-tiktok-computer-prep | Google 访问、Chrome、Google 账号、NotebookLM |
| captain-tiktok-device-reset | 手机准备、爱思助手及保留的独立初始化资料 |
| captain-tiktok-apple-id | 保留的独立 Apple ID 教学 |
| captain-tiktok-shadowrocket-treehole | 保留的独立手机网络教学 |
| captain-tiktok-ip-purchase | 保留的独立 IP 采购资料 |
| captain-tiktok-ip-diagnostics | 保留的独立 IP 检测资料 |
| captain-tiktok-operations | 保留的独立运营诊断 |
| captain-tiktok-shop | 保留的独立店铺教学 |
| captain-tiktok-governance | 维护、审查、发布及恢复规则 |

保留其他模块不代表课前入口可以自动调用其框架外能力。模块数量和名称没有调整。

## 使用与依赖

需要支持读取本地 `SKILL.md` 的 AI 宿主。将所需 Skill 文件夹放入该宿主支持的技能目录，并保持它们互为同级目录，以便解析相对引用。仅把 ZIP 发给聊天网页不代表已安装。

课前流程至少一起提供 `captain-tiktok`、`captain-tiktok-computer-prep`、`captain-tiktok-device-reset` 三个模块；功能模块依赖总入口的流程契约，不是零依赖单文件。此仓库保留全部模块，未附适用于所有 AI 的通用安装命令，也未验证所有客户端。

Windows/Mac 指学员电脑操作流程。其他 AI 平台是否支持安装和调用 Skill，以其实际能力为准。Markdown 指令不是程序级访问控制，无法保证每个模型都绝不偏离。

## 本地校验

校验脚本仅使用 Python 3 标准库，不联网、不安装依赖、不修改文件：

```sh
python3 scripts/validate.py
```

Windows 可将 `python3` 换为已安装的 `python`。校验内容包括文件校验值、模块清单、相对文件引用、动作顺序和关键规则回归。静态校验不能替代真实模型行为测试。

## 上传 GitHub

把本目录内容上传到你自己的仓库，保留文件夹层级，包括 `.gitignore`。不要把外层工作区、以前的 ZIP、账户凭据、订阅、二维码或软件安装包一并上传。

本次只生成本地源码，不创建远程仓库、不推送、不自动部署。根目录 `SHA256SUMS.txt` 只校验 Skill 正文与元数据，新增的仓库说明和校验脚本不在该清单内。修改已列文件后需重新生成其校验值，不能把校验失败当作发布通过。

## 测试与授权说明

已进行本地结构和静态规则校验；维护者在对话中走通了主流程。没有完成本轮独立模型边界测试或各平台安装实测，不承诺所有场景无误。

未替维护者选择开源许可证。上传到公开仓库不等于自动授予开源许可；正式开源前需确认资料、教程链接和联系方式的公开授权，并自行选择合适的许可证。
