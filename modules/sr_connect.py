import time
import serial

def connect():
    ser = serial.Serial('/dev/ttyUSB0', timeout=0)
    ser.baudrate = 115200

    time.sleep(1)
    ser.write(b'\r')

    time.sleep(1)
    ser.write(b'root\r')

    time.sleep(1)
    ser.write(b'Admin123\r')

    time.sleep(1)
    ser.write(b'ls /etc\r')

    time.sleep(1)
    output = ser.read(100).decode('utf-8', 'ignore')
    print(output)

