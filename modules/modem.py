import sys
sys.dont_write_bytecode = True

import time


def get_modem_ssh(channel):

    try:
        channel.send("/etc/init.d/gsmd start\n")
        time.sleep(2)
        channel.recv(1024)
        channel.send("gsmctl -w\n")
        time.sleep(1)
        lines = channel.recv(1024).decode().splitlines()
        modem_name = lines[1]

        channel.send("gsmctl -m\n")
        time.sleep(1)
        lines = channel.recv(1024).decode().splitlines()
        modem_model = lines[1]

        modem_row = {f"Modem name: {modem_name}\nModem model: {modem_model}\n"}

        return modem_row
    except:
        modem_name = "Could not get modem name"
        modem_model = "Could not get modem model"
        modem_row = {f"Modem name: {modem_name} Modem model: {modem_model}\n"}

        return modem_row



def get_modem_ser(ser_client):
    try:
        time.sleep(1)
        ser_client.write(b'/etc/init.d/gsmd start\r')
        time.sleep(1)
        ser_client.reset_input_buffer()
        time.sleep(1)
        ser_client.write(b'gsmctl -w\r')
        time.sleep(1)
        lines = ser_client.read(100).decode('utf-8', 'ignore').splitlines()
        modem_name = lines[1]

        time.sleep(1)
        ser_client.write(b'gsmctl -m\r')
        time.sleep(1)
        lines = ser_client.read(100).decode('utf-8', 'ignore').splitlines()
        modem_model = lines[1]
        print(modem_name)
        modem_row = {f"Modem name: {modem_name}\nModem model: {modem_model}\n"}

        return modem_row

        
    except:
        modem_name = "Could not get modem name"
        modem_model = "Could not get modem model"
        modem_row = {f"Modem name: {modem_name} Modem model: {modem_model}\n"}

        return modem_row
