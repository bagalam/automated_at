import time
from modules import connection
from modules import device_check
from modules import cmd_test
from modules import modem


def main():
    
    print(f"Chose a connection.\n1. LAN connection.\n2.Serial connection. (Run whith sudo)\n(Type exit to exit)")
    option = input() 
    match option:
        case "1":
            ssh_client = connection.connect_ssh()
            if(ssh_client != False):

                stdin, stdout, sterr = ssh_client.exec_command("cat /proc/sys/kernel/hostname")
                stdin.close()
                dev_name = stdout.read().decode().strip()

                modem_name, modem_model = modem.get_modem(ssh_client)
                modem_row = {f"Modem name: {modem_name}Modem model: {modem_model}"}

                stdin, stdout, sterr = ssh_client.exec_command("/etc/init.d/gsmd stop")
                stdin.close()

                print(f"Product being tested: {dev_name}")

                time.sleep(5)
                commands, channel = device_check.check_device(dev_name, ssh_client)

                cmd_test.test_cmd(commands, channel, dev_name, modem_row)

                stdin, stdout, sterr = ssh_client.exec_command("/etc/init.d/gsmd start")
                stdin.close()
                ssh_client.close()
            else:
                print("Could not connect to device")
        case "2":
            ser_client = connection.connect_ser()
            if(ser_client != False):
                # ser_client.write(b'cat /proc/sys/kernel/hostname')
                # output = ser_client.read(100).decode('utf-8', 'ignore')
                # print(output)
                # ser_client.close()
                print("Connected")
            else:
                print("Connection failed")
        case "exit" | "Exit":
            quit()

if __name__ == "__main__":
    main()