import os
import urllib.request

# 定义数据源
SOURCES = {
    "IPv4": {
        "all_cn": "https://ispip.clang.cn/all_cn.txt",
        "chinatelecom": "https://ispip.clang.cn/chinatelecom.txt",
        "unicom_cnc": "https://ispip.clang.cn/unicom_cnc.txt",
        "cmcc": "https://ispip.clang.cn/cmcc.txt",
        "chinabtn": "https://ispip.clang.cn/chinabtn.txt",
        "cernet": "https://ispip.clang.cn/cernet.txt",
        "gwbn": "https://ispip.clang.cn/gwbn.txt",
        "othernet": "https://ispip.clang.cn/othernet.txt",
        "hk": "https://ispip.clang.cn/hk.txt",
        "mo": "https://ispip.clang.cn/mo.txt",
        "tw": "https://ispip.clang.cn/tw.txt"
    },
    "IPv6": {
        "all_cn_ipv6": "https://ispip.clang.cn/all_cn_ipv6.txt",
        "chinatelecom_ipv6": "https://ispip.clang.cn/chinatelecom_ipv6.txt",
        "unicom_cnc_ipv6": "https://ispip.clang.cn/unicom_cnc_ipv6.txt",
        "cmcc_ipv6": "https://ispip.clang.cn/cmcc_ipv6.txt",
        "chinabtn_ipv6": "https://ispip.clang.cn/chinabtn_ipv6.txt",
        "cernet_ipv6": "https://ispip.clang.cn/cernet_ipv6.txt",
        "gwbn_ipv6": "https://ispip.clang.cn/gwbn_ipv6.txt",
        "othernet_ipv6": "https://ispip.clang.cn/othernet_ipv6.txt",
        "hk_ipv6": "https://ispip.clang.cn/hk_ipv6.txt",
        "mo_ipv6": "https://ispip.clang.cn/mo_ipv6.txt",
        "tw_ipv6": "https://ispip.clang.cn/tw_ipv6.txt"
    }
}

def download_and_convert():
    # 切换当前工作目录到项目根目录（脚本在 py/ 目录下，.. 代表上一级）
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    for version in ["IPv4", "IPv6"]:
        os.makedirs(os.path.join(base_dir, version, "txt"), exist_ok=True)
        os.makedirs(os.path.join(base_dir, version, "rsc"), exist_ok=True)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    for version, urls in SOURCES.items():
        ros_cmd = "/ip firewall address-list" if version == "IPv4" else "/ipv6 firewall address-list"

        for name, url in urls.items():
            print(f"正在处理 {version} : {name}...")
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=15) as response:
                    content = response.read().decode('utf-8')
                
                ip_list = [line.strip() for line in content.splitlines() if line.strip() and not line.startswith('#')]

                if not ip_list:
                    print(f"警告：{name} 未获取到有效IP，跳过。")
                    continue

                # 1. 保存纯文本 txt
                txt_path = os.path.join(base_dir, version, "txt", f"{name}.txt")
                with open(txt_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(ip_list) + "\n")

                # 2. 生成 RouterOS rsc
                rsc_path = os.path.join(base_dir, version, "rsc", f"{name}.rsc")
                list_name = f"List_{name}"
                
                rsc_lines = []
                rsc_lines.append(f"{ros_cmd} remove [find list={list_name}]")
                
                for ip in ip_list:
                    rsc_lines.append(f"{ros_cmd} add address={ip} comment=\"\" disabled=no list={list_name}")
                
                with open(rsc_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(rsc_lines) + "\n")

            except Exception as e:
                print(f"处理 {name} 时出错: {e}")

if __name__ == "__main__":
    download_and_convert()