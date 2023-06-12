import sys
sys.dont_write_bytecode = True

import time
import paramiko
from modules.file_modules import read_config_file

def modem_name(channel):
    try:
        channel.recv(1024)
        channel.send("ATI\n")
        time.sleep(1)
        lines = channel.recv(1024).decode().splitlines()
        modem_name = lines[2]
        modem_model = lines[4]

        modem_row = {f"Modem name: {modem_name}\nModem model: {modem_model}\n"}

        return modem_row
    except:
        modem_name = "Could not get modem name"
        modem_model = "Could not get modem model"
        modem_row = {f"Modem name: {modem_name} Modem model: {modem_model}\n"}

        return modem_row


def modem(name, ssh_client, path):

    commands = read_config_file.get_commands(name, path)
    if(commands == False):
        print("Device not suported")
    else:
        channel = ssh_client.get_transport().open_session()
        channel.get_pty()
        channel.invoke_shell()
        channel.send("socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\r")
        time.sleep(1)
        channel.send("/etc/init.d/gsmd stop\n")
        time.sleep(1)
        modem_row = modem_name(channel)
        return commands, channel, modem_row

def connect(ip, user, pswd, po):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip,port=po,username=user,password=pswd)

        stdin, stdout, sterr = ssh_client.exec_command("/etc/init.d/gsmd stop")
        stdout.flush()
        stdin.close()
        return ssh_client
    except:
        return False

