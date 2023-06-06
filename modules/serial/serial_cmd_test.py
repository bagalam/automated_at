import sys
sys.dont_write_bytecode = True

import time
from modules import rw_file
from modules import console_write
from modules import connect_modem

def check_output(out_lines, tests, rows, command):
    if out_lines[-2] or out_lines[-1] == "OK":
        result = "OK"
        tests[0] += 1
    else:
        result = "Error"
        tests[1] += 1

    console_write.print_current(command, result, tests)
    row = {"command":command, "Expected result":"OK", "Got result":result}
    rows.append(row)

def receive(ser_client, command, rows, tests):
    while True:
        time.sleep(1)
        out_lines = ser_client.read(200).decode('utf-8', 'ignore').splitlines()
        if out_lines:
            check_output(out_lines, tests, rows, command)
        else:
            break
                        
    

def test_cmd(ser_client, dev_name):
    tests= [0,0]
    rows = []

    time.sleep(2)
    ser_client.reset_input_buffer()
    time.sleep(2)

    print(f"Product being tested: {dev_name}")

    commands, modem_row = connect_modem.serial_modem(dev_name, ser_client)

    ser_client.reset_input_buffer()
    time.sleep(2)

    try:
        for command in commands:
            try:
                time.sleep(1)
                ser_client.write((command + '\r').encode())
                receive(ser_client, command, rows, tests)
            except:
                break
    except TypeError:
        print("Could not get the commands")

    time.sleep(1)
    ser_client.write(b'\x03')
    rw_file.write_to_file(rows, dev_name, modem_row)

    console_write.print_tests(tests)