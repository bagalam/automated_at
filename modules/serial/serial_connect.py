import sys
sys.dont_write_bytecode = True

import time
import serial

def connect_ser(username, pswd, name):
    if "TRM2" in name or "trm2" in name:
        try:
            ser = serial.Serial('/dev/ttyUSB3', timeout=0, baudrate=115200)
            return ser
        except:
            return False
    else:
        try:
            ser = serial.Serial('/dev/ttyUSB0', timeout=0, baudrate=115200)
            time.sleep(1)
            ser.write((username + '\r').encode())

            time.sleep(1)
            ser.write((pswd + '\r').encode())

            time.sleep(1)
            ser.write(b'/etc/init.d/gsmd stop\r')

            return ser
        except:
            return False