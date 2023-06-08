import sys
sys.dont_write_bytecode = True

import json

def get_commands(name, path):

    with open(path, "r") as read_file:
        command_file = json.load(read_file)
    if "RUT9" in name or "rut9" in name:
        return command_file["RUT9"]
    elif "RUTX" in name or "rutx" in name:
        return command_file["RUTX"]
    elif "TRM2" in name or "trm2" in name:
        return command_file["TRM2"]
    else:
        return False