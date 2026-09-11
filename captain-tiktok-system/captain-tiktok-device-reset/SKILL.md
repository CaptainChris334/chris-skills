---
name: captain-tiktok-device-reset
description: "处理 iPhone 设备准备、爱思助手清空刷机、刷机成功验收和刷机后的手机初始化。默认只处理设备准备；只有用户明确询问刷机时才进入刷机流程。"
---

# 设备与初始化

## 工作方式

先读取 [references/phone-devices.md](references/phone-devices.md) 判断设备。默认完成设备选择、购买注意事项和爱思助手下载，但不执行刷机；只有用户明确输入“刷机”或询问刷机时，才读取 [references/mobile-foundation.md](references/mobile-foundation.md) 执行刷机和初始化。进入爱思助手下载流程时，不要求先判断 Windows 的 x64 或 ARM64 类型，直接按官网提供的 Windows 安装包下载即可。每完成一个页面要求打码截图，确认后再继续。

## 关键流程

- 爱思助手智能刷机中选择目标系统版本和“清空”。
- 点击“开始刷机”，确认后点击“立即刷机”。
- 出现绿色对勾、“恭喜您，刷机成功啦～”和“完成”才算电脑端刷机成功。
- 手机初始化选择“不传输 App 与数据”，Apple ID 按 SOP 处理。
- 定位、分析、隐私和权限按已提供截图 SOP 执行；不确定当前页面时要求截图。
- 刷机不是硬件准备阶段的默认步骤；网络配置归入后续软件阶段。

## 资料

- 设备选择与刷机初始化：[references/phone-devices.md](references/phone-devices.md)、[references/mobile-foundation.md](references/mobile-foundation.md)
