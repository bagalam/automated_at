import sys
sys.dont_write_bytecode = True

import time
import serial

def connect_ser(username, pswd):
    try:
        ser = serial.Serial('/dev/ttyUSB0', timeout=0)
        ser.baudrate = 115200

        time.sleep(1)
        ser.write((username + '\r').encode())

        time.sleep(1)
        ser.write((pswd + '\r').encode())

        return ser
    except:
        return False