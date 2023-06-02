import time
from modules import connection
from modules import device_check
from modules import cmd_test
from modules import modem
from modules import serial_cmd_test


def main():
    
    print(f"Chose a connection.\n1. LAN connection.\n2. Serial connection. (Run whith sudo)\n(Type exit to exit)")
    option = input() 

    match option:
        case "1":
            ssh_client = connection.connect_ssh()
            if(ssh_client != False):
                stdin, stdout, sterr = ssh_client.exec_command("/etc/init.d/gsmd stop")
                stdin.close()

                cmd_test.test_cmd(ssh_client)

                ssh_client.close()
            else:
                print("Could not connect to device")
        case "2":
            ser_client = connection.connect_ser()
            if(ser_client != False):
                time.sleep(1)
                ser_client.write(b'/etc/init.d/gsmd stop\r')
                time.sleep(1)
                ser_client.read(200)

                serial_cmd_test.test_cmd(ser_client)
                
                time.sleep(1)
                ser_client.write(b'exit\r')

                ser_client.close()
            else:
                print("Could not connect to device")
        case "exit" | "Exit":
            quit()

if __name__ == "__main__":
    main()