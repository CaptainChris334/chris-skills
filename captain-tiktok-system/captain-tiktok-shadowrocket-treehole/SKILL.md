---
name: captain-tiktok-shadowrocket-treehole
description: "处理 Shadowrocket 小火箭与树洞订阅链路：二维码导入、节点选择、Socks5 代理添加、Proxy Pass 设置、连接开关和网页连通性验收。"
---

# Shadowrocket 与树洞

## 工作方式

先读取 [总入口流程控制契约](../captain-tiktok/SKILL.md#流程控制契约全局硬规则)，继承当前步骤、状态和待返回位置。跳过、临时答疑、前置阻塞及结束条件按总入口执行；缺少该依赖时不猜测控制规则、不继续顺序陪跑。模块内按现有 SOP 的独立结果建立固定节点编号，不能用“跳过”一次略过整套流程。

读取 [references/relay.md](references/relay.md)。设备初始化完成后由总入口衔接本 Skill；不复制设备初始化规则。引导用户一次完成一个动作，每一步截图确认。

## 关键流程

- 树洞后台选择 iPhone OS 和 Shadowrocket 订阅。
- 小火箭左上角扫码导入。
- 展开订阅并选择目标节点。
- 单独 IP 参数通过右上角 `+` 添加，类型按服务商要求；当前示例为 `Socks5`。
- 填写 Address、Port、Username、Password。
- Proxy Pass 优先选择新加坡或日本树洞节点。
- 保存后选择代理，打开右上角开关，`Global Routing` 设为 `Proxy`。

不在对话中复述完整订阅链接、认证参数、UUID 或密码。
