import time
from modules import ssh_connection
from modules import device_check
from modules import cmd_test
from modules import modem


def main():
    ssh_client = ssh_connection.connect()

    stdin, stdout, sterr = ssh_client.exec_command("cat /proc/sys/kernel/hostname")
    stdin.close()
    dev_name = stdout.read().decode().strip()

    modem_name, modem_model = modem.get_modem(ssh_client)
    modem_row = {"modem name":modem_name, "modem model":modem_model}

    stdin, stdout, sterr = ssh_client.exec_command("/etc/init.d/gsmd stop")
    stdin.close()

    print(f"Product being tested: {dev_name}")

    time.sleep(5)
    commands, channel = device_check.check_device(dev_name, ssh_client)

    cmd_test.test_cmd(commands, channel, dev_name)

    stdin, stdout, sterr = ssh_client.exec_command("/etc/init.d/gsmd start")
    stdin.close()
    ssh_client.close()

if __name__ == "__main__":
    main()