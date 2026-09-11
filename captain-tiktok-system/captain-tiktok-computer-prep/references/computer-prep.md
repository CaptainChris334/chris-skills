# 第二阶段：软件下载与电脑端准备

## 使用原则

这一阶段只负责电脑端基础搭建。AI 必须先告知网址，再告诉学员使用电脑当前已有的浏览器复制、粘贴到地址栏并回车；Windows 默认使用 Edge，Mac 默认使用 Safari，Chrome 安装完成后再统一使用 Chrome。不要让学员直接点击聊天中的跳转链接，也不要让学员自行搜索陌生下载站。

每完成一个关键步骤，要求学员上传截图，AI 确认当前页面后再继续。截图必须遮住密码、验证码、完整订阅链接、UUID、私钥、二维码、支付信息和账号恢复信息。

## 固定网址

Chrome 官方下载：

```text
https://www.google.cn/chrome/
```

粉猫 Clash Verge Rev 官方下载：

```text
https://github.com/clash-verge-rev/clash-verge-rev/releases
```

爱思助手官网：

```text
https://www.i4.cn
```

树洞导航站：

```text
https://nihaoshudong.com
```

树洞登录页（导航地址变化时，以导航站为准）：

```text
https://dash.gwshudong.com/auth/login
```

Google 账号购买入口：

```text
https://www.humkt.com
```

购买后登录和修改 SOP：

```text
https://gcnvra3kee7w.feishu.cn/wiki/Fr7ewDdMRi6Ga6kiD2ecropInA3?from=from_copylink
```

## 陪装顺序

### 1. 安装粉猫

将官方地址复制到电脑当前浏览器的地址栏并打开：

```text
https://github.com/clash-verge-rev/clash-verge-rev/releases
```

打开页面后：

1. 找到最新正式版本，避开名称带 `alpha`、`beta` 或 `rc` 的测试版本；
2. 向下滑动当前版本页面；
3. 找到“下载地址”或页面底部的 `Assets` 区域；
4. 根据电脑系统和芯片类型选择安装包；
5. 不要下载 `Source code (zip)`、`Source code (tar.gz)`、Linux 或其他系统版本；
6. 下载后先核对文件名，再进行安装。

先让学员上传系统信息截图：

- Windows 普通 Intel/AMD：选择 `x64`
- Windows ARM：选择 `ARM64`
- Mac M 芯片：选择 `aarch64`
- Mac Intel：选择 `x64`

让学员上传下载文件名截图，再指导安装。Windows 安装被安全中心拦截时，先看具体提示和保护历史，不默认关闭整个安全中心。Mac 出现“文件已损坏”时，先确认来源和版本，再按 [references/clients.md](clients.md) 的安全流程处理。

#### Windows 安装路径

1. 在 GitHub 的“下载地址”或 `Assets` 区域选择 Windows 安装包。
2. 普通 Intel/AMD 电脑选择文件名带 `x64` 的版本。
3. Windows ARM 电脑选择文件名带 `arm64` 或 `ARM64` 的版本。
4. 优先选择安装包格式（如 `.msi` 或官方提供的 `.exe`），不要下载源码压缩包。
5. 下载完成后双击安装包，按安装向导完成安装。
6. 打开“Clash Verge Rev”，上传软件首页截图。
7. 如果 Windows 安全中心拦截，打开“Windows 安全中心”→“病毒和威胁防护”→“保护历史记录”，上传拦截提示截图；不要直接关闭整个安全中心。

#### Mac 安装路径

1. 点击屏幕左上角苹果图标，进入“关于本机”，查看芯片类型。
2. Apple M1、M2、M3、M4 等 Apple 芯片下载文件名带 `aarch64` 的 `.dmg`。
3. Intel 芯片下载文件名带 `x64` 的 `.dmg`。
4. 不要下载 Windows、Linux 或 `Source code` 文件。
5. 双击 `.dmg`，将 `Clash Verge Rev` 拖入 `Applications`。
6. 从“应用程序”中打开软件，上传首页截图。

如果提示“无法打开”、开发者无法验证或应用被阻止：

1. 先确认安装包来自上面的官方 GitHub Releases 页面；
2. 打开“系统设置”；
3. 进入“隐私与安全性”；
4. 向下找到被阻止的 `Clash Verge Rev`；
5. 点击“仍要打开”，再确认打开。

只有确认文件来自官方 GitHub，并且“仍要打开”仍无法解决时，才使用终端命令：

1. 按 `Command + 空格键` 打开 Spotlight；
2. 输入 `Terminal` 或“终端”并回车；
3. 复制并执行：

```bash
sudo xattr -cr "/Applications/Clash Verge Rev.app"
```

4. 输入 Mac 开机密码并回车。输入密码时终端不会显示星号或字符，这是正常现象；
5. 再从“应用程序”中打开 `Clash Verge Rev`。

如果 macOS 明确提示应用会损害电脑、包含恶意软件或文件已被篡改，不执行终端命令，停止安装并上传提示截图。

不确定 Windows 架构或 Mac 芯片类型时，先上传“系统信息/关于本机”截图，不要凭设备外观猜版本。

### 2. 访问树洞并购买

粉猫安装成功后，让学员使用电脑当前已有的浏览器复制树洞导航地址。Chrome 尚未安装时，Windows 使用 Edge，Mac 使用 Safari；Chrome 安装完成后再统一切换到 Chrome。进入导航站的国内访问或最新地址入口，再注册/登录树洞。

登录后：

1. 进入“购买套餐”。
2. 选择 `PRO 套餐`。
3. 选择周期并完成支付。
4. 刷新页面确认套餐生效。

购买页面提示原套餐可能被覆盖、剩余时间可能不保留，套餐流量不累计；购买前让学员先截图当前套餐状态。

### 3. 获取并导入订阅

购买成功后进入树洞的节点列表或订阅入口，具体按钮以学员截图为准。不要要求学员把完整订阅链接发到对话框。

接着打开粉猫：

1. 进入“订阅”或“Profiles”页面；
2. 找到订阅框；
3. 粘贴订阅链接；
4. 点击“导入”；
5. 导入后点击“刷新订阅”；
6. 等待节点列表出现。

不要把完整订阅链接发给 AI。完成后回复：

```text
订阅已导入
```

如果找不到订阅入口，请截图发给 AI。

### 4. 连接和验证

订阅已成功导入后：

1. 点击“代理”；
2. 在已导入的节点中，点击右侧箭头展开节点列表；
3. 选择一个延迟最低的节点；
4. 点击“设置”；
5. 打开“系统代理”开关；
6. 打开“统一延迟”开关。

完成后回复：

```text
节点已连接
```

如果节点显示 `Timeout`、`Error` 或无法连接，可以截图给 AI，也可以告诉 AI 具体提示。

使用电脑当前已有的浏览器测试普通网页和 Google。Chrome 尚未安装时，Windows 使用 Edge，Mac 使用 Safari。

Google 打不开时，按顺序检查：节点是否超时、是否误选直连、系统代理是否开启、规则模式是否异常、订阅是否过期；一次只改一个变量。不要把电脑端节点直接当成后续 TikTok 手机运营 IP。

### 5. 安装 Chrome

Windows 先打开 Edge，Mac 先打开 Safari。复制 Chrome 地址，粘贴到地址栏并回车。下载并安装后，打开 Chrome，上传首页截图。

Chrome 是后续统一浏览器，用于访问购买入口、SOP 页面和 NotebookLM。

### 6. 购买并完善 Google 账号

请打开 Chrome，将下面网址复制到地址栏：

```text
https://www.humkt.com
```

注册账号，进入后选择 Google 账号产品。购买前确认：

1. 购买美国地区账号；
2. 满一年的优先；
3. 价格控制在 30 以内；
4. 官网有购买流程，购买后按照流程操作；
5. 如果仍然不会购买或使用，联系船长工作人员。

购买完成后回复：

```text
Google 账号已购买
```

不要把账号密码、验证码或恢复码发给 AI。

### 7. 登录 NotebookLM

打开 NotebookLM 官方页面，使用已经完善好的 Google 账号登录。登录成功后上传首页截图。

### 8. 电脑端整体验收

确认以下项目：

- 粉猫可以打开；
- 树洞订阅已经导入并完成配置；
- 节点可以连接；
- 普通网页和 Google 可以访问；
- Chrome 可以正常打开；
- Google 账号资料已完成修改；
- NotebookLM 可以正常登录。

## 第二阶段完成标准

学员能够：

- 打开 Chrome；
- 打开粉猫；
- 登录树洞并确认 PRO 套餐；
- 导入树洞订阅；
- 选择节点并开启系统代理；
- 用 Chrome 正常访问普通网页和 Google；
- 完成 Google 账号资料修改；
- 成功登录 NotebookLM；
- 课前准备工作完成，停止主动引导后续流程。

完成验收后只回复：

```text
课前准备工作已完成，请调整好心态，准备开课，祝你学习顺利！
```

不要主动引导手机网络配置、IP 配置或 TikTok 运营。只有学员之后主动提问时，才按对应 Skill 响应。
