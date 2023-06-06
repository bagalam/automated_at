import sys
sys.dont_write_bytecode = True

import paramiko

def connect_ssh(ip, user, pswd):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip,port=22,username=user,password=pswd)

        stdin, stdout, sterr = ssh_client.exec_command("/etc/init.d/gsmd stop")
        stdout.flush()
        stdin.close()
        return ssh_client
    except:
        return False

