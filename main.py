import sys
sys.dont_write_bytecode = True

from modules import flags
from modules.ssh import ssh_connect
from modules.serial import serial_connect
from modules.ssh import ssh_cmd_test
from modules.serial import serial_cmd_test


def main():
    args = flags.flags()
    

    if args.hostname:
        ssh_client = ssh_connect.connect(args.hostname, args.username, args.password, args.port)
        if(ssh_client != False):
            ssh_cmd_test.test_cmd(ssh_client, args.name, args.path)

            ssh_client.close()
        else:
            print("Could not connect to device")
    else:
        ser_client = serial_connect.connect(args.usb, args.baudrate)
        if(ser_client != False):
            serial_cmd_test.test_cmd(ser_client, args.name, args.path)

            ser_client.close()
        else:
            print("Could not connect to device")

if __name__ == "__main__":
    main()