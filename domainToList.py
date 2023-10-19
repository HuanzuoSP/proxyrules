# 读取域名列表文件
with open('./domain/ecsDirect.txt', 'r') as file:
    domains = file.read().splitlines()

# 生成 .list 格式的文件
with open('./domain/ecsDirect.list', 'w') as output_file:
    for domain in domains:
        if domain:
            output_file.write(f"DOMAIN,{domain}\n")
