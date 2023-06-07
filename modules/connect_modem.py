import sys
sys.dont_write_bytecode = True

import time
from modules import rw_file

def lan_modem_name(channel):
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


def serial_modem_name(ser_client, name):
    try:
        ser_client.reset_input_buffer()
        time.sleep(1)
        ser_client.write(b'ATI\r')
        time.sleep(1)
        lines = ser_client.read(100).decode('utf-8', 'ignore').splitlines()
        if "TRM2" in name or "trm2" in name:
            modem_name = lines[0]
            modem_model = lines[1]
        else:
            modem_name = lines[2]
            modem_model = lines[3]
        modem_row = {f"Modem name: {modem_name}\nModem model: {modem_model}\n"}

        return modem_row

        
    except:
        modem_name = "Could not get modem name"
        modem_model = "Could not get modem model"
        modem_row = {f"Modem name: {modem_name} Modem model: {modem_model}\n"}

        return modem_row

def lan_modem(name, ssh_client):

    commands = rw_file.get_commands(name)
    if(commands == False):
        print("Device not suported")
    else:
        channel = ssh_client.get_transport().open_session()
        channel.get_pty()
        channel.invoke_shell()
        channel.send("socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\r")
        time.sleep(1)
        modem_row = lan_modem_name(channel)
        return commands, channel, modem_row
    
def serial_modem(name, ser_client):

    commands = rw_file.get_commands(name)
    if(commands == False):
        print("Device not suported")
    else:
        if "TRM2" in name or "trm2" in name:
            modem_row = serial_modem_name(ser_client, name)
            return commands, modem_row
        else:
            time.sleep(1)
            ser_client.write(b'socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\r')
            time.sleep(1)
            ser_client.write(b'AT+QCSQ=0\n')
            time.sleep(3)
            modem_row = serial_modem_name(ser_client)
            return commands, modem_row
        