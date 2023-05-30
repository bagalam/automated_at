import serial

def connect():
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = 'ttyUSB0'
    ser.open()