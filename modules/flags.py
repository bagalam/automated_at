import sys
sys.dont_write_bytecode = True

import argparse
import os

current_directory = os.getcwd()
relative_path = "modules/config.json"
path = os.path.join(current_directory, relative_path)

def flags():
    parser = argparse.ArgumentParser()
    parser.add_argument("-host","--hostname", help="Hostname, lan or public ip, to connect to.", type=str)
    parser.add_argument("-p","--port", help="Connection port", type=int, default=22)
    parser.add_argument("-n", "--name", help="Device name", type=str, required=True)
    parser.add_argument("-u","--username", help="Username to log in to the device", type=str, default="root", required=False)
    parser.add_argument("-pswd","--password", help="Password to log in to the device", type=str, default="Admin123", required=False)
    parser.add_argument("-baud","--baudrate", help="Baudrate when connecting via serial cable", type=int, default=115200)
    parser.add_argument("-path", help="Path to the config file", type=str, default=path)
    parser.add_argument("-usb", help="Specify wich usb port should the program connect to. Default is /dev/ttyUSB0", type=str, default="/dev/ttyUSB0")

    args = parser.parse_args()

    return args