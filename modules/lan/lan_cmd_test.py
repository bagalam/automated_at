import sys
sys.dont_write_bytecode = True

import time
from modules import rw_file
from modules import console_write
from modules import modem
from modules import connect_modem

def check_output(out_lines, tests, rows, command):
    if out_lines[-2] == "OK":
        result = "OK"
        tests[0] += 1
    else:
        result = "Error"
        tests[1] += 1

    console_write.print_current(command, result, tests)
    row = {"command":command, "Expected result":"OK", "Got result":result}
    rows.append(row)

def receive(channel, command, rows, tests):
    while True:
        if channel.recv_ready():
            output = channel.recv(1024)

            out_lines = output.decode().splitlines()
            check_output(out_lines, tests, rows, command)
                
        else:
            time.sleep(0.5)
            if not(channel.recv_ready()):
                break


def test_cmd(ssh_client, dev_name):
    tests= [0,0]
    rows = []

    print(f"Product being tested: {dev_name}")

    time.sleep(1)
    commands, channel = connect_modem.check_device_ssh(dev_name, ssh_client)

    for command in commands:
        try:
            channel.send("$>" + command + "\n")
            receive(channel, command, rows, tests)
        except:
            break
    channel.send('\x03')
    modem_row = modem.get_modem_ssh(channel)
    rw_file.write_to_file(rows, dev_name, modem_row)

    console_write.print_tests(tests)