import paramiko
import time
import serial

def connect_ssh():
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname="192.168.1.1",port=22,username="root",password="Admin123")
        return ssh_client
    except:
        return False
    
def connect_ser():
    try:
        ser = serial.Serial('/dev/ttyUSB0', timeout=0)
        ser.baudrate = 115200

        time.sleep(1)
        ser.write(b'root\r')

        time.sleep(1)
        ser.write(b'Admin123\r')

        time.sleep(2)
        ser.write(b'ls /etc \r')
        #ser.flush()

        time.sleep(1)
        output = ser.read(10000).decode('utf-8', 'ignore')
        print(output)

        time.sleep(1)
        ser.write(b'exit\r')
        print("Connected to device")

        return ser
    except:
        return False

