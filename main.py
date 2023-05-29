from modules import ssh_connection
from modules import device_check
from modules import cmd_test



def main():
    ssh_client = ssh_connection.connect()
    stdin, stdout, sterr = ssh_client.exec_command("cat /proc/sys/kernel/hostname")
    stdin.close
    dev_name = stdout.read().decode().strip()
    print(f"Product being tested: {dev_name}")
    commands, channel = device_check.check_device(dev_name, ssh_client)
    cmd_test.test_cmd(commands, channel, dev_name)
    
    ssh_client.close()

if __name__ == "__main__":
    main()