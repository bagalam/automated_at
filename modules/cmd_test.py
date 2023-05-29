import time
from modules import rw_file

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
    print(f"Tests passed: {passed}\nTests not passed: {errors}\nTotal commands: {passed+errors}")