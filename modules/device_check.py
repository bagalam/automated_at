import time
from modules import rw_file

def check_device_ssh(name, ssh_client):

    commands = rw_file.get_commands(name)
    if(commands == False):
        print("Device not suported")
    else:
        channel = ssh_client.get_transport().open_session()
        channel.get_pty()
        channel.invoke_shell()
        channel.send("socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\r")
        return commands, channel
    
def check_device_ser(name, ser_client):

    print(name)
    commands = rw_file.get_commands(name)
    if(commands == False):
        print("Device not suported")
    else:
        time.sleep(1)
        ser_client.write(b'socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\r')
        time.sleep(3)
        ser_client.write(b'AT+QCSQ=0')
        time.sleep(1)
        left = ser_client.inWaiting()
        ser_client.read(left)
        return commands