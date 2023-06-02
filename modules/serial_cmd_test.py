import time
from modules import rw_file
from modules import console_write
from modules import modem
from modules import device_check

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

def receive(ser_client, command, rows, tests):
    while True:
        time.sleep(1)
        out_lines = ser_client.read(200).decode('utf-8', 'ignore').splitlines()
        print(out_lines)
        if out_lines:
            check_output(out_lines, tests, rows, command)
        else:
            break
                        
    

def test_cmd(ser_client):
    tests= [0,0]
    rows = []

    time.sleep(2)
    ser_client.write(b'cat /proc/sys/kernel/hostname\r')

    time.sleep(1)
    lines = ser_client.read(100).decode('utf-8', 'ignore').splitlines()
    print(lines)
    dev_name = lines[1]

    print(dev_name)

    commands = device_check.check_device_ser(dev_name, ser_client)

    for command in commands:
        try:
            time.sleep(0.5)
            ser_client.write((command + '\r').encode())
            receive(ser_client, command, rows, tests)
        except:
            break
    time.sleep(1)
    ser_client.write(b'\x03')
    modem_row = modem.get_modem_ser(ser_client)
    rw_file.write_to_file(rows, dev_name, modem_row)

    console_write.print_tests(tests)