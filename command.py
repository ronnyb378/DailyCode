import subprocess  

list_files = subprocess.run('ls')
home = subprocess.run(['cd', '~'])
list_files = subprocess.run('ls')

