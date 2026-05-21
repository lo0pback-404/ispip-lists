import os
import urllib.request

# 精确定义映射关系：[文件名] -> (数据源URL, RouterOS列表名称)
IP_CONFIG = {
    "IPv4": {
        "all_cn": ("https://ispip.clang.cn/all_cn.txt", "List_ALL_China"),
        "chinatelecom": ("https://ispip.clang.cn/chinatelecom.txt", "List_ALL_ChinaTelecom"),
        "unicom_cnc": ("https://ispip.clang.cn/unicom_cnc.txt", "List_ALL_ChinaUnicom"),
        "cmcc": ("https://ispip.clang.cn/cmcc.txt", "List_ALL_ChinaMobile"),
        "chinabtn": ("https://ispip.clang.cn/chinabtn.txt", "List_ALL_ChinaBtn"),
        "cernet": ("https://ispip.clang.cn/cernet.txt", "List_ALL_ChinaCernet"),
        "gwbn": ("https://ispip.clang.cn/gwbn.txt", "List_ALL_ChinaGwbn"),
        "othernet": ("https://ispip.clang.cn/othernet.txt", "List_Other_China"),
        "hk": ("https://ispip.clang.cn/hk.txt", "List_ALL_HK"),
        "mo": ("https://ispip.clang.cn/mo.txt", "List_ALL_MO"),
        "tw": ("https://ispip.clang.cn/tw.txt", "List_ALL_TW")
    },
    "IPv6": {
        "all_cn_ipv6": ("https://ispip.clang.cn/all_cn_ipv6.txt", "List_ALL_China"),
        "chinatelecom_ipv6": ("https://ispip.clang.cn/chinatelecom_ipv6.txt", "List_ALL_ChinaTelecom"),
        "unicom_cnc_ipv6": ("https://ispip.clang.cn/unicom_cnc_ipv6.txt", "List_ALL_ChinaUnicom"),
        "cmcc_ipv6": ("https://ispip.clang.cn/cmcc_ipv6.txt", "List_ALL_ChinaMobile"),
        "chinabtn_ipv6": ("https://ispip.clang.cn/chinabtn_ipv6.txt", "List_ALL_ChinaBtn"),
        "cernet_ipv6": ("https://ispip.clang.cn/cernet_ipv6.txt", "List_ALL_ChinaCernet"),
        "gwbn_ipv6": ("https://ispip.clang.cn/gwbn_ipv6.txt", "List_ALL_ChinaGwbn"),
        "othernet_ipv6": ("https://ispip.clang.cn/othernet_ipv6.txt", "List_Other_China"),
        "hk_ipv6": ("https://ispip.clang.cn/hk_ipv6.txt", "List_ALL_HK"),
        "mo_ipv6": ("https://ispip.clang.cn/mo_ipv6.txt", "List_ALL_MO"),
        "tw_ipv6": ("https://ispip.clang.cn/tw_ipv6.txt", "List_ALL_TW")
    }
}

def download_and_convert():
    # 定位到项目根目录
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    for version in ["IPv4", "IPv6"]:
        os.makedirs(os.path.join(base_dir, version, "txt"), exist_ok=True)
        os.makedirs(os.path.join(base_dir, version, "rsc"), exist_ok=True)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    for version, items in IP_CONFIG.items():
        # 根据版本确定首行路径
        ros_base_cmd = "/ip firewall address-list" if version == "IPv4" else "/ipv6 firewall address-list"

        for file_name, (url, list_name) in items.items():
            print(f"正在同步 {version} -> 文件: {file_name}.txt/.rsc | 列表名: {list_name}")
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=15) as response:
                    content = response.read().decode('utf-8')
                
                # 过滤并清洗IP
                ip_list = [line.strip() for line in content.splitlines() if line.strip() and not line.startswith('#')]

                if not ip_list:
                    print(f"提示：{file_name} 未捕获到有效IP，略过。")
                    continue

                # 1. 写入纯文本 TXT
                txt_path = os.path.join(base_dir, version, "txt", f"{file_name}.txt")
                with open(txt_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(ip_list) + "\n")

                # 2. 紧凑格式写入 RouterOS RSC (移除首行 remove，剥离前缀)
                rsc_path = os.path.join(base_dir, version, "rsc", f"{file_name}.rsc")
                
                rsc_lines = []
                rsc_lines.append(ros_base_cmd) # 第一行声明路径
                
                for ip in ip_list:
                    rsc_lines.append(f"add address={ip} comment=\"\" disabled=no list={list_name}")
                
                with open(rsc_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(rsc_lines) + "\n")

            except Exception as e:
                print(f"处理发生异常 [{file_name}]: {e}")

if __name__ == "__main__":
    download_and_convert()
