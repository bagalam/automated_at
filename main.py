import sys
import os
sys.dont_write_bytecode = True

from modules import flags

import importlib

def main():
    args = flags.flags()
    con = args.connection
    con = con.lower()

    module = importlib.import_module(f'modules.{con}.connect')
    cmd_test = importlib.import_module(f'modules.{con}.cmd_test')
    try:
        client = module.connect(args.hostname, args.username, args.password, args.port)
    except:
        os.system("service ModemManager stop")
        client = module.connect(args.usb, args.baudrate)

    cmd_test.test_cmd(client, args.name, args.path)

    client.close()


if __name__ == "__main__":
    main()