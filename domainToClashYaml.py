import jinja2
from datetime import datetime
import os

# 获取当前脚本文件的绝对路径
script_dir = os.path.dirname(__file__)

# 获取文件夹列表，只包括 'domain' 和 'domain-suffix' 文件夹
folder_names = [folder for folder in os.listdir('.') if os.path.isdir(folder) and folder in ['domain', 'domain-suffix']]

# 获取当前系统时间并格式化为字符串
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

for folder_name in folder_names:
    # 构建 Clash 配置数据
    folder_path = os.path.join(script_dir, folder_name)

    # 创建模板加载器和模板环境
    template_loader = jinja2.FileSystemLoader(searchpath=[script_dir, os.path.join(script_dir, folder_name)])
    env = jinja2.Environment(loader=template_loader)

    # 获取文件夹中的域名列表文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt") and filename != 'recorded_domains.txt':
          
            with open(os.path.join(folder_path, filename), 'r') as file:
                domains = file.read().splitlines()

            # 构建目标路径，将扩展名从 .txt 替换为 .yaml
            target_filename = filename.replace(".txt", ".yaml")
            
            # 构建 Clash 配置数据
            clash_config = {
                "name": target_filename,
                "author": "HuanzuoSP",
                "repo": "https://github.com/HuanzuoSP/proxyrules/" + folder_name + "/" + target_filename,
                "updated": current_time,
                "total_domains": len(domains),
                "domains": domains,
            }

            # 渲染模板并写入 Clash 配置文件
            with open(os.path.join(folder_path, target_filename), 'w') as yaml_file:
                yaml_file.write(env.get_template(f"{folder_name}.j2").render(clash_config))

            with open(os.path.join(folder_path, filename.replace(".txt", ".list")), 'w') as list_file:
                for domain in domains:
                    if folder_name == "domain":
                        list_file.write(f"DOMAIN,{domain}\n")
                    else:
                        list_file.write(f"DOMAIN-SUFFIX,{domain}\n")