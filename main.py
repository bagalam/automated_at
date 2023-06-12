import sys
import os
sys.dont_write_bytecode = True

from modules import flags

import importlib

def main():
    args = flags.flags()
    

    if args.hostname:
        ssh_module = importlib.import_module('modules.ssh.ssh_connect')
        ssh_cmd_test = importlib.import_module('modules.ssh.ssh_cmd_test')

        ssh_client = ssh_module.connect(args.hostname, args.username, args.password, args.port)
        if(ssh_client != False):
            ssh_cmd_test.test_cmd(ssh_client, args.name, args.path)

            ssh_client.close()
        else:
            print("Could not connect to device")
    else:
        serial_connect = importlib.import_module('modules.serial.serial_connect')
        serial_cmd_test = importlib.import_module('modules.serial.serial_cmd_test')

        ser_client = serial_connect.connect(args.usb, args.baudrate)
        if(ser_client != False):
            serial_cmd_test.test_cmd(ser_client, args.name, args.path)

            ser_client.close()
        else:
            print("Could not connect to device")

if __name__ == "__main__":
    main()