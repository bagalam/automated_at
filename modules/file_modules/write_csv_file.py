import sys
sys.dont_write_bytecode = True

import csv
import datetime

def write_to_file(rows, name, modem_row):
    date = datetime.datetime.now()
    date = date.strftime(f"%y_%m_%d_%X")

    fields = ["command", "Expected result", "Got result", "Test passed/failed"]
    
    with open(f"log/{name}_{date}.csv", "w", newline='') as file:
        file.writelines(modem_row)
        writer = csv.DictWriter(file, fieldnames= fields)
        writer.writeheader()
        writer.writerows(rows)