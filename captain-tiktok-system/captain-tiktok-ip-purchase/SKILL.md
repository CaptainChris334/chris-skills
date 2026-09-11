---
name: captain-tiktok-ip-purchase
description: "指导选择和购买 TikTok 业务所需的目标地区 IP：东南亚优先 911Proxy，欧美优先 Miya 或 IPRoyal，并核对静态住宅、ISP、独享、城市和 ASN 等规格。"
---

# IP 购买

## 工作方式

读取 [references/purchase-specifications.md](references/purchase-specifications.md)。先确认目标国家、城市、产品类型、ASN、数量和周期，再指导用户核对订单页面；IP 质量检测由 `captain-tiktok-ip-diagnostics` 负责。

## 当前业务口径

- 东南亚：优先 `911Proxy`。
- 欧美：优先 `Miya` 或 `IPRoyal`。
- 优先目标地区匹配、长期稳定、独享的静态住宅或 ISP。
- 避免 Hosting、Datacenter、Cloud、VPS，除非目标产品就是该类型。

购买后只确认 Address、Port、Username、Password、协议类型等字段是否齐全，不要求用户把完整参数发给 AI。
