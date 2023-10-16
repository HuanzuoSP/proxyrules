import jinja2
import yaml
from datetime import datetime
import os

# 获取当前脚本文件的绝对路径
script_dir = os.path.dirname(__file__)

# 构建模板文件的绝对路径
template_file_path = os.path.join(script_dir, "ecsdirect.j2")

# 创建模板环境
template_loader = jinja2.FileSystemLoader(searchpath=script_dir)
env = jinja2.Environment(loader=template_loader)
template = env.get_template("ecsdirect.j2")

# 您的 GitHub 仓库链接
github_repo = "https://github.com/HuanzuoSP/YourRepo"

# 获取文件名列表，排除 recorded_domains.txt
file_names = [filename for filename in os.listdir('.') if filename.endswith('.txt') and filename != 'recorded_domains.txt']

# 获取当前系统时间并格式化为字符串
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

for txt_filename in file_names:
    # 构建 Clash 配置数据
    yaml_filename = txt_filename.replace('.txt', '.yaml')
    
    with open(txt_filename, 'r') as file:
        domains = file.read().splitlines()
    # 构建 Clash 配置数据
    clash_config = {
        "name": file_names,
        "author": "HuanzuoSP",
        "repo": github_repo,
        "updated": current_time,
        "total_domains": len(domains),
        "domains": domains,
    }

# 渲染模板并写入 Clash 配置文件
rendered_config = template.render(clash_config)

target_path = os.path.join('/data', yaml_filename)
    
with open(target_path, 'w') as yaml_file:
    yaml_file.write(rendered_config)