import sys
sys.dont_write_bytecode = True

import argparse
import time
from modules.lan import lan_connect
from modules.serial import serial_connect
from modules.lan import lan_cmd_test
from modules.serial import serial_cmd_test


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-l","--lan", help="Device lan ip address to connect via lan.", type=str)
    parser.add_argument("-n", "--name", help="Device name", type=str, required=True)
    parser.add_argument("-u","--username", help="Username to log in to the device", type=str, required=True)
    parser.add_argument("-pswd","--password", help="Password to log in to the device", type=str, required=True)

    args = parser.parse_args()
    

    if args.lan:
        ssh_client = lan_connect.connect_ssh(args.lan, args.username, args.password)
        if(ssh_client != False):
            stdin, stdout, sterr = ssh_client.exec_command("/etc/init.d/gsmd stop")
            stdin.close()

            lan_cmd_test.test_cmd(ssh_client, args.name)

            ssh_client.close()
        else:
            print("Could not connect to device")
    else:
        ser_client = serial_connect.connect_ser(args.username, args.password)
        if(ser_client != False):
            time.sleep(1)
            ser_client.write(b'/etc/init.d/gsmd stop\r')

            serial_cmd_test.test_cmd(ser_client, args.name)
            
            time.sleep(1)
            ser_client.write(b'exit\r')

            ser_client.close()
        else:
            print("Could not connect to device")

if __name__ == "__main__":
    main()