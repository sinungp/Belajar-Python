import paramiko

host = "IP ADDR"
port = 22
username = "USERNAME"
password = "PASSWORD"

command = "sudo -S -p '' reboot"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
stdin.write('colokcabut\n')
stdin.flush()

lines = stdout.readlines()
print(lines)
 
