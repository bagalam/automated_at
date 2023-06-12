import sys
sys.dont_write_bytecode = True

import time
from modules import console_write
from modules.ssh import ssh_connect
from modules.file_modules import write_csv_file

def check_output(out_lines, tests, rows, command):
    if out_lines[-2] == command['excpected']:
        passed = "Passed"
        tests[0] += 1
    else:
        passed = "Failed"
        tests[1] += 1

    console_write.print_current(command, out_lines[-2], tests)
    row = {"command":command['command'], "Expected result":command['excpected'], "Got result":out_lines[-2], "Test passed/failed": passed}
    rows.append(row)

def receive(channel, command, rows, tests):
    while True:
        if channel.recv_ready():
            output = channel.recv(1024)
            out_lines = output.decode().splitlines()
        else:
            time.sleep(0.5)
            if not(channel.recv_ready()):
                break
    check_output(out_lines, tests, rows, command)


def test_cmd(ssh_client, dev_name, path):
    tests= [0,0]
    rows = []

    print(f"Product being tested: {dev_name}")

    time.sleep(1)
    commands, channel, modem_row = ssh_connect.modem(dev_name, ssh_client, path)

    for command in commands:
        try:
            channel.send("$>" + command['command'] + "\n")
            receive(channel, command, rows, tests)
        except:
            break
    channel.send('\x03')
    channel.send("/etc/init.d/gsmd start\n")
    write_csv_file.write_to_file(rows, dev_name, modem_row)
    console_write.print_tests(tests)