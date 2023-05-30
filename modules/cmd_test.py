import time
import colorama
from modules import rw_file

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

def receive(channel, command, rows, tests):
    while True:
                if channel.recv_ready():
                    output = channel.recv(1024)

                    out_lines = output.decode().splitlines()

                    if out_lines[-2] == "OK":
                        result = out_lines[-2]
                        tests[0] += 1
                    else:
                        result = "Error"
                        tests[1] += 1

                    print(f"{command} {result}")
                    row = {"command":command, "Expected result":"OK", "Got result":result}
                    rows.append(row)
                        
                else:
                    time.sleep(0.5)
                    if not(channel.recv_ready()):
                        break
    

def test_cmd(commands, channel, dev_name, modem_row):
    tests= [0,0]
    rows = []
    
    for command in commands:
        try:
            channel.send("$>" + command + "\n")
            receive(channel, command, rows, tests)
        except:
            break

    rw_file.write_to_file(rows, dev_name, modem_row)

    prGreen(f"Tests passed: {tests[0]}")
    prRed(f"Tests not passed: {tests[1]}")
    print(f"Total commands: {tests[0]+tests[1]}")