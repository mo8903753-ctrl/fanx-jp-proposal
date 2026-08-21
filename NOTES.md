# FanX Drive X3 · 日本 Makuake 提案 — 定案口径

## 定价（用户拍板 2026-08-21）
规则：日本销量最多档 = KS Launch Special × 1.2，日元尾数 X,800/X9,800，160 JPY/USD 折美元展示，正文零日文零日元。

- 零售锚点（一般贩售预定价格）：¥26,800 = $167.50（KS MSRP $169）
- 24小时限定 ¥16,800 = $105.00 · 37% OFF（首日 24h 时间限）
- 超早鸟 ¥17,800 = $111.25 · 34% OFF
- **早鸟 ¥18,800 = $117.50 · 30% OFF（主销档，= $99×1.2 口径）**
- Makuake限定 ¥19,800 = $123.75 · 26% OFF（不限量长尾）
- 2台套装 ¥35,800 = $223.75 · 33% OFF
- 首日优惠券必写（折扣率待品牌方确认）
- 512GB / 1TB 预装版按同一 +20% 口径另行定价（KS：$199/$279）

## 目标双档（skill 日本模块强制 $500K/$1M，预算 16.31%/18.34%）
$500K 档销量拆分（支持者 4,100 人 · 加权 AOV $122.07 · 达成率 100.1%）：
- 24h限定 400 台 = $42,000
- 超早鸟 600 台 = $66,750（限量 600）
- 早鸟 1,900 台 = $223,250（限量 1,900）
- Makuake限定 1,000 台 = $123,750（不限量）
- 2台套装 200 组 = $44,750（限量 200 组）
- 合计 $500,500；早鸟+Makuake限定 = 2,900/4,100 = 70.7% ≥60% ✓
$1M 档 = 数量全×2（8,200 人 / $1,001,000）。

## 预算 $500K 档（16.31%，行项比例不动）
预热广告 5.25%=$26,250 · 上线广告 10.00%=$50,000 · 媒体&KOL 0.62%=$3,100 · PR TIMES ¥33,000=$206 · 线下展示 ¥250,000=$1,563 · 其他工具 ¥61,803=$386 → 合计 $81,505（16.3%）
$1M 档（18.34%）：53,000/120,000/7,000/300/2,500/600 → $183,400
预热 Leads：$26,250 ÷ CPL $3–4 ≈ 6,600–8,800 条；预热转化取 5%（区间 3–8%）

## KS 事实（已核实，2026-08-21 产品 agent 复核版）
FanX Drive X3：HK$682,854（美国访客显示 $87,068）/ 689 backers / 均价 HK$991 / 2026-08-11→09-25 45 天 / 1741%
正确链接：kickstarter.com/projects/fanxiang/fanx-drive-turn-your-pc-into-a-private-cloud-nasin-minutes（kicktraq 同 slug）
公司：Fanxiang 梵想，深圳 Lingdechuang（领德创，非 Lingdechuan）；香港主体 GUOSEN TECHNOLOGY
档位：×1 首发 $99($169,41%OFF，526/600) · ×1 SEB $109(36%) · ×1 EB $119(30%) · ×2 首发 $199 · ×2 SEB $209(38%) · 512GB 首发 $199($259,23%) · 1TB 首发 $279($369,24%) · 全球免邮 · 2026-11 交付 · 3 年质保
规格：78×54×10mm 58g · ESP32 · Wi-Fi 4 · USB-C（速度等级未公布，勿承诺速率）· DC5V/1A · 带智能小屏 · 铝合金 · 语言含日语 · 包装：本体+USB-A转C+C2C线+指南
⚠️ 必须连主机用，非独立 NAS；机身不能自装硬盘；主机端首发仅 Windows，macOS 主机支持承诺 2026-11 软件更新（deck 一律写「现有电脑」不写 Mac）
卖点 8 个：Remote Wakeup(WoL) / Remote Desktop / Docker / OpenClaw(本地跑AI) / AI Album / App Center 50+ / Home Media Hub / AES-256 / 无订阅费
海外评价：NASCompares 200K（有真视频 youtube.com/watch?v=g48oAepJQls）/ NASeros 246K / SpineCard 305K / Tech Magnet 468K / Yendry Cayo 3.5M / 911Reviews 1.17M
BackerGuardian 信任分 51/100：KS 账号新、「World's First」被质疑（deck 已避开首创性表述）

## 图片素材（本机）
- hero：/tmp/fanx-img/img02.png（竖版 526×900 主视觉，dark bg，含 8 icon）→ hero 用 contain+深色底
- 规格表：img30.png（竖版）
- 海外 KOL 评价卡：img04-09（英文，可直接嵌）
- 信任徽章：img01.png；发货/税费表：img29.png
- 公司/案例图：从 /tmp/gordix-index.html 提取 base64 复用
- UGREEN 截图：assets/ugreen-us.jpg / ugreen-jp.jpg
- 受众照片：等 agent 返回 URL → wsrv.nl 下载 → 压缩嵌入

## 章节结构（13 章）
01 封面 / 02 品类判断·产品证明 / 03 竞品与比较（日本已上架：UGREEN NASync 等） / 04 合作模式 / 05 目标拆解 / 06 $500K/$1M 试算 / 07 定价档位 / 08 受众 / 09 营销预算+KOL（id="n-kol"）/ 10 时间线（60/90 天两档）/ 11 公司 / 12 案例资源 / 13 可行性+收尾

## 避坑记录
- KS 签名图 URL 会过期（img22 已废）→ 素材全部 base64 内嵌，不热链
- agent 读图被 provider 拒 → 图片一律主线程 sips 压缩后分批 Read
- GitHub 大文件用 gh api base64 单行推送；不用 contents API 拉 >1MB 文件
- 正文禁假名/¥/円（QA 用 innerText 正则扫）；日文 Return 文案是独立交付物不进 deck
- 风险章已删；订金/Secret Reward/Late Pledge/Launch Special/Early Bird 英文字样不出现

## KOL 章与交付状态（2026-08-21 收尾）
- `src/05b-kol.html`：6 频道卡（头部=吉田製作所Y/なおたろ，腰部=かじがや電器店/ワタナベカズマサ/せろりんね/散財TV）+ 候选说明 note（递补 とモヤシ→こにたく→Aile Ch.）；头像 kolNa.jpg、封面 kolNv.jpg（wsrv.nl 代理下载，ytc/ 前缀 URL 必须整体 urlencode）
- KOL 卡片内日文频道名/视频标题按专有名词与事实引用豁免；QA 扫描把 n-kol→下一章区间排除后再扫假名/¥/円
- 构建 3867KB / 11 parts / 51 张 data:image；sections 12/12 闭合；无 .mstrip
- 已部署：https://fanx-jp-proposal.vercel.app（alias）/ fanx-jp-proposal-iclcrumc1-mo8903753-9751s-projects.vercel.app
- 已推送：github.com/mo8903753-ctrl/fanx-jp-proposal@main（本次 git push 直连成功，未用 gh api 绕行）
- 待办：首日优惠券折扣率待品牌方确认后填入；递补频道存储视频二轮核实（如需全存储主题阵容）
