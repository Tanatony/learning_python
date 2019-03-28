import subprocess

print(subprocess.run('ls'))
print(subprocess.run('pwd'))
print(subprocess.run('who'))
print(subprocess.run(['ping', '-c', '3', '-n', '8.8.8.8']))
