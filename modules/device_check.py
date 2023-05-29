from modules import rw_file

def check_device(name, ssh_client):

    commands = rw_file.get_commands(name)
    if(commands == False):
        print("Device not suported")
    else:
        channel = ssh_client.get_transport().open_session()
        channel.get_pty()
        channel.invoke_shell()
        channel.send("socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\r")
        return commands, channel