# China IP Address Lists for RouterOS v7

这是一个基于 GitHub Actions 自动运行的中国大陆及各运营商 IP 地址列表同步仓库。系统每日清晨自动从上游数据源获取最新数据，在保留原始 `txt` 格式的同时，自动转化为适用于 MikroTik RouterOS v7 处理的紧凑型 `.rsc` 防火墙地址列表（Address List）脚本。

本工具旨在为网络管理员提供精细化的企业多线 BGP/策略路由优化方案。

## 📢 数据源声明
本仓库产生的所有基础数据，均每日全量同步自公共数据源：[ispip.clang.cn](https://ispip.clang.cn/)。本仓库仅做数据格式的分流转换与自动化打包。

## 📁 目录结构
```text
├── IPv4/
│   ├── txt/      # 纯文本 IPv4 子网列表
│   └── rsc/      # 紧凑型 RouterOS v7 导入脚本
└── IPv6/
    ├── txt/      # 纯文本 IPv6 子网列表 (带 _ipv6 后缀)
    └── rsc/      # 紧凑型 RouterOS v7 IPv6 导入脚本
```

## 🚀 快捷下载与 CDN 加速直链 (Direct Downloads)

以下链接均已接入 `jsDelivr` 全球 CDN 加速网络。

| 运营商/区域描述 | IPv4 纯文本 | IPv4 ROS 脚本 | IPv6 纯文本 | IPv6 ROS 脚本 |
| :--- | :---: | :---: | :---: | :---: |
| 🇨🇳 **中国大陆全网** | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/txt/all_cn.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/rsc/all_cn.rsc) | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/txt/all_cn_ipv6.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/rsc/all_cn_ipv6.rsc) |
| ⚡ **中国电信** | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/txt/chinatelecom.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/rsc/chinatelecom.rsc) | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/txt/chinatelecom_ipv6.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/rsc/chinatelecom_ipv6.rsc) |
| 🌀 **中国联通** | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/txt/unicom_cnc.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/rsc/unicom_cnc.rsc) | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/txt/unicom_cnc_ipv6.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/rsc/unicom_cnc_ipv6.rsc) |
| Ⓜ️ **中国移动** | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/txt/cmcc.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/rsc/cmcc.rsc) | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/txt/cmcc_ipv6.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/rsc/cmcc_ipv6.rsc) |
| 📡 **中国广电** | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/txt/chinabtn.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/rsc/chinabtn.rsc) | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/txt/chinabtn_ipv6.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/rsc/chinabtn_ipv6.rsc) |
| 🎓 **中国教育网** | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/txt/cernet.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/rsc/cernet.rsc) | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/txt/cernet_ipv6.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/rsc/cernet_ipv6.rsc) |
| 🌐 **鹏博士/长宽** | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/txt/gwbn.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/rsc/gwbn.rsc) | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/txt/gwbn_ipv6.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/rsc/gwbn_ipv6.rsc) |
| ➕ **其他ISP** | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/txt/othernet.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/rsc/othernet.rsc) | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/txt/othernet_ipv6.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/rsc/othernet_ipv6.rsc) |
| 🇭🇰 **中国香港** | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/txt/hk.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/rsc/hk.rsc) | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/txt/hk_ipv6.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/rsc/hk_ipv6.rsc) |
| 🇲🇴 **中国澳门** | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/txt/mo.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/rsc/mo.rsc) | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/txt/mo_ipv6.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/rsc/mo_ipv6.rsc) |
| 🇹🇼 **中国台湾** | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/txt/tw.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/rsc/tw.rsc) | [TXT直链](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/txt/tw_ipv6.txt) | [RSC脚本](https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/rsc/tw_ipv6.rsc) |

*注：导入 RouterOS 后内部生成的 Address List 名称，IPv4 与 IPv6 保持完全一致（不带 `_ipv6` 后缀），方便策略路由及防火墙规则统一过滤。*

## ⚙️ RouterOS 自动维护示例

您可以在 RouterOS 中通过 `System -> Scheduler` 配置定时任务，使用 CDN 链接实现无缝、高速的自动更新。

### 示例 1：定时拉取中国大陆全网 IPv4 列表（通过 jsDelivr 加速）
```ortand
# 1. 高速下载最新的紧凑型 rsc 文件
/tool fetch url="https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv4/rsc/all_cn.rsc" dst-path=all_cn.rsc

# 2. 清理历史产生的该列表条目
/ip firewall address-list remove [find list=all_cn]

# 3. 导入新路由数据
/import file-name=all_cn.rsc
```

### 示例 2：定时拉取中国电信 IPv6 列表（通过 jsDelivr 加速）
```ortand
# 1. 高速下载最新的紧凑型 IPv6 rsc 文件
/tool fetch url="https://cdn.jsdelivr.net/gh/lo0pback-404/ispip-lists@main/IPv6/rsc/chinatelecom_ipv6.rsc" dst-path=chinatelecom_ipv6.rsc

# 2. 清理历史产生的 IPv6 该列表条目
/ipv6 firewall address-list remove [find list=chinatelecom]

# 3. 导入新路由数据
/import file-name=chinatelecom_ipv6.rsc
```

## ⚖️ 免责声明与合规性

1. 本项目所引用的上游基础数据均来源于公共合规网络诊断、路由分发等公开技术源。
2. 本项目产生的所有数据列表和转换脚本**仅供网络日常运维、多线策略路由优化、BGP 路由表路径分流及学术研究**之用。
3. 严禁利用本项目产生的数据从事任何违反当地法律法规及互联网络管理条例的行为。用户在使用本项目数据进行网络基础架构调整时需自行承担相应责任。
