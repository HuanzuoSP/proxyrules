import subprocess

# 调用第一个脚本
subprocess.run(['python', 'domainToClashYaml.py'])

# 调用第二个脚本
subprocess.run(['python', 'domainToList.py'])
