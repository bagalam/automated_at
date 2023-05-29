import time
import colorama
from modules import rw_file

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

def test_cmd(commands, channel, dev_name):
    passed = 0
    errors = 0
    rows = []
    for command in commands:
        try:
            channel.send("$>" + command + "\n")
            while True:
                if channel.recv_ready():
                    output = channel.recv(1024)

                    out_lines = output.decode().splitlines()

                    if out_lines[-2] == "OK":
                        result = out_lines[-2]
                        passed += 1
                    else:
                        result = "Error"
                        errors += 1

                    print(f"{command} {result}")
                    row = {"command":command, "Expected result":"OK", "Got result":result}
                    rows.append(row)
                        
                else:
                    time.sleep(0.5)
                    if not(channel.recv_ready()):
                        break
        except:
            break
    rw_file.write_to_file(rows, dev_name)
    prGreen(f"Tests passed: {passed}")
    prRed(f"Tests not passed: {errors}")
    print(f"Total commands: {passed+errors}")