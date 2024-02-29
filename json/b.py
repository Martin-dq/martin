import requests

base_url = "http://api.hclyz.com:81/mf"
response_url = "http://api.hclyz.com:81/mf/json.txt"
output_file = "output.m3u8"

# 获取response_url中的JSON数据
response = requests.get(response_url)
data = response.json()

# 获取"pingtai"列表
pingtai_list = data["pingtai"]

with open(output_file, 'w') as f:
    for item in pingtai_list:
        address = item["address"]
        full_url = f"{base_url}/{address}"
        f.write(f"#EXTINF:-1,tvg-logo=\"{item['xinimg']}\" group-title=\"{address}\"\n")
        f.write(f"{full_url}\n")

print("M3U8文件已生成")