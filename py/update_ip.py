import os
import urllib.request

# 精确定义映射关系：[下载URL] -> (配置版本, 文件名后缀, 内部ROS列表名称)
# 通过分离开文件名和列表名，完美实现：文件名带 _ipv6，而内部 listname 不带 _ipv6
IP_CONFIG = {
    # IPv4 数据源
    "https://ispip.clang.cn/all_cn.txt": ("IPv4", "", "List_ALL_China"),
    "https://ispip.clang.cn/chinatelecom.txt": ("IPv4", "", "List_ALL_ChinaTelecom"),
    "https://ispip.clang.cn/unicom_cnc.txt": ("IPv4", "", "List_ALL_ChinaUnicom"),
    "https://ispip.clang.cn/cmcc.txt": ("IPv4", "", "List_ALL_ChinaMobile"),
    "https://ispip.clang.cn/chinabtn.txt": ("IPv4", "", "List_ALL_ChinaBtn"),
    "https://ispip.clang.cn/cernet.txt": ("IPv4", "", "List_ALL_ChinaCernet"),
    "https://ispip.clang.cn/gwbn.txt": ("IPv4", "", "List_ALL_ChinaGwbn"),
    "https://ispip.clang.cn/othernet.txt": ("IPv4", "", "List_Other_China"),
    "https://ispip.clang.cn/hk.txt": ("IPv4", "", "List_ALL_HK"),
    "https://ispip.clang.cn/mo.txt": ("IPv4", "", "List_ALL_MO"),
    "https://ispip.clang.cn/tw.txt": ("IPv4", "", "List_ALL_TW"),

    # IPv6 数据源
    "https://ispip.clang.cn/all_cn_ipv6.txt": ("IPv6", "_ipv6", "List_ALL_China"),
    "https://ispip.clang.cn/chinatelecom_ipv6.txt": ("IPv6", "_ipv6", "List_ALL_ChinaTelecom"),
    "https://ispip.clang.cn/unicom_cnc_ipv6.txt": ("IPv6", "_ipv6", "List_ALL_ChinaUnicom"),
    "https://ispip.clang.cn/cmcc_ipv6.txt": ("IPv6", "_ipv6", "List_ALL_ChinaMobile"),
    "https://ispip.clang.cn/chinabtn_ipv6.txt": ("IPv6", "_ipv6", "List_ALL_ChinaBtn"),
    "https://ispip.clang.cn/cernet_ipv6.txt": ("IPv6", "_ipv6", "List_ALL_ChinaCernet"),
    "https://ispip.clang.cn/gwbn_ipv6.txt": ("IPv6", "_ipv6", "List_ALL_ChinaGwbn"),
    "https://ispip.clang.cn/othernet_ipv6.txt": ("IPv6", "_ipv6", "List_Other_China"),
    "https://ispip.clang.cn/hk_ipv6.txt": ("IPv6", "_ipv6", "List_ALL_HK"),
    "https://ispip.clang.cn/mo_ipv6.txt": ("IPv6", "_ipv6", "List_ALL_MO"),
    "https://ispip.clang.cn/tw_ipv6.txt": ("IPv6", "_ipv6", "List_ALL_TW")
}

def download_and_convert():
    # 定位到项目根目录
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    for version in ["IPv4", "IPv6"]:
        os.makedirs(os.path.join(base_dir, version, "txt"), exist_ok=True)
        os.makedirs(os.path.join(base_dir, version, "rsc"), exist_ok=True)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    for url, (version, suffix, list_name) in IP_CONFIG.items():
        # 组装独立的文件名（例如：List_ALL_China_ipv6）
        file_name = f"{list_name}{suffix}"
        
        # 根据版本确定 RouterOS 首行命令路径
        ros_base_cmd = "/ip firewall address-list" if version == "IPv4" else "/ipv6 firewall address-list"

        print(f"正在同步 {version} -> 文件名: {file_name} | 内部List名: {list_name}")
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as response:
                content = response.read().decode('utf-8')
            
            # 过滤并清洗 IP 数据
            ip_list = [line.strip() for line in content.splitlines() if line.strip() and not line.startswith('#')]

            if not ip_list:
                print(f"提示：{file_name} 未捕获到有效IP，略过。")
                continue

            # 1. 写入纯文本 TXT
            txt_path = os.path.join(base_dir, version, "txt", f"{file_name}.txt")
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write("\n".join(ip_list) + "\n")

            # 2. 写入紧凑格式 RouterOS RSC
            rsc_path = os.path.join(base_dir, version, "rsc", f"{file_name}.rsc")
            
            rsc_lines = []
            rsc_lines.append(ros_base_cmd) # 第一行声明路径（/ip... 或 /ipv6...）
            
            for ip in ip_list:
                # 这里的 list={list_name} 确保了即使是 v6 文件，其内部依然绑定不带 _ipv6 的标准名称
                rsc_lines.append(f"add address={ip} comment=\"\" disabled=no list={list_name}")
            
            with open(rsc_path, "w", encoding="utf-8") as f:
                f.write("\n".join(rsc_lines) + "\n")

        except Exception as e:
            print(f"处理发生异常 [{file_name}]: {e}")

if __name__ == "__main__":
    download_and_convert()
