import paramiko

host = "10.10.5.20"
port = 22
username = "astro"
password = "colokcabut"

command = "sudo -S -p '' reboot"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
stdin.write('colokcabut\n')
stdin.flush()

lines = stdout.readlines()
print(lines)
 