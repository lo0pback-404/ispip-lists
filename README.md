# China IP Address Lists for RouterOS v7

这是一个基于 GitHub Actions 自动运行的中国大陆及各运营商 IP 地址列表同步仓库。系统每日清晨自动从上游数据源获取最新数据，在保留原始 `txt` 格式的同时，自动转化为适用于 MikroTik RouterOS v7 处理的紧凑型 `.rsc` 防火墙地址列表（Address List）脚本。

本工具旨在为网络管理员提供精细化的企业多线 BGP/策略路由优化方案。

## 📢 数据源声明
本仓库产生的所有基础数据，均每日全量同步自公共数据源：[ispip.clang.cn](https://ispip.clang.cn/)。本仓库仅做数据格式的分流转换与自动化打包。

## 📁 目录结构
```text
├── IPv4/
│   ├── txt/      # 纯文本 IPv4 子网列表 (以列表名称命名)
│   └── rsc/      # 紧凑型 RouterOS v7 导入脚本
└── IPv6/
    ├── txt/      # 纯文本 IPv6 子网列表 (带 _ipv6 后缀)
    └── rsc/      # 紧凑型 RouterOS v7 IPv6 导入脚本
