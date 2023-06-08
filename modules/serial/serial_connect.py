import sys
sys.dont_write_bytecode = True

from modules.file_modules import read_config_file
import time
import serial

def serial_modem_name(ser_client):
    try:
        ser_client.write(b'ATE1\r')
        time.sleep(1)
        ser_client.reset_input_buffer()
        time.sleep(1)
        ser_client.write(b'ATI\r')
        time.sleep(1)
        lines = ser_client.read(100).decode('utf-8', 'ignore').splitlines()
        print(lines)
        modem_name = lines[2]
        modem_model = lines[3]
        modem_row = {f"Modem name: {modem_name}\nModem model: {modem_model}\n"}

        return modem_row 
    except:
        modem_name = "Could not get modem name"
        modem_model = "Could not get modem model"
        modem_row = {f"Modem name: {modem_name} Modem model: {modem_model}\n"}

        return modem_row

def serial_modem(name, ser_client, path):

    commands = read_config_file.get_commands(name, path)
    if(commands == False):
        print("Device not suported")
    else:
        modem_row = serial_modem_name(ser_client)
        return commands, modem_row

def connect(usb, baud):
    try:
        ser = serial.Serial(usb, timeout=0, baudrate=baud)
        return ser
    except:
        return False