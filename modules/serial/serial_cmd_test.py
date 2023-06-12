import sys
sys.dont_write_bytecode = True

import time
from modules.file_modules import write_csv_file
from modules import console_write
from modules.serial import serial_connect

def check_output(out_lines, tests, rows, command):
    if out_lines[-1] == command['excpected']:
        passed = "Passed"
        tests[0] += 1
    else:
        passed = "Failed"
        tests[1] += 1

    console_write.print_current(command, out_lines[-1], tests)
    row = {"command":command['command'], "Expected result":command['excpected'], "Got result":out_lines[-1], "Test passed/failed": passed}
    rows.append(row)

def receive(ser_client, command, rows, tests):
    while True:
        time.sleep(1)
        if ser_client.inWaiting() > 0:
            data_to_read = ser_client.inWaiting()
            out_lines = ser_client.read(data_to_read).decode('utf-8', 'ignore').splitlines()
        else:
            break
    check_output(out_lines, tests, rows, command)
                        
    

def test_cmd(ser_client, dev_name, path):
    tests= [0,0]
    rows = []

    print(f"Product being tested: {dev_name}")

    commands, modem_row = serial_connect.modem(dev_name, ser_client, path)

    ser_client.reset_input_buffer()
    time.sleep(2)

    try:
        for command in commands:
            try:
                ser_client.write((command['command'] + '\r').encode())
                receive(ser_client, command, rows, tests)
            except:
                break
    except TypeError:
        print("Could not get the commands")

    write_csv_file.write_to_file(rows, dev_name, modem_row)

    console_write.print_tests(tests)