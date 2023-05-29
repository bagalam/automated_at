import csv
import json
import os
import datetime

def write_to_file(rows, name):
    date = datetime.datetime.now()
    date = date.strftime(f"%y\%m\%d_%X")

    fields = ["command", "Expected result", "Got result"]

    with open(f"1task/log/{name}_{date}.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames= fields)
        writer.writeheader()
        writer.writerows(rows)

def get_commands(name):
    current_directory = os.getcwd()
    relative_path = "1task/modules/config.json"
    cmd_path = os.path.join(current_directory, relative_path)
    with open(cmd_path, "r") as read_file:
        command_file = json.load(read_file)
    if "RUT9" in name:
        return command_file["RUT9"]
    elif "RUTX" in name:
        return command_file["RUTX"]
    else:
        return False