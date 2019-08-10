import csv
import sys
import time
from os import path

class Logger:

    def __init__(self):

        assert len(sys.argv) > 1

        self.path = None
        for arg in sys.argv:
            if "--config=" in arg:
                firstsplit = arg.split("=")[1]
                index = firstsplit.rfind("/")
                self.path = firstsplit[:index] + "/logs.csv" #LOOK AT NAMING, LOOK AT SLASH
                #initialize column nuames
                break

        assert self.path is not None

#output a csv instead
    def log(self, logs, framenum = time.time()):
        logs["frame"] = framenum
        if not path.exists(self.path):
            with open(self.path, mode='w') as logfile:
                fieldnames = logs.keys()
                writer = csv.DictWriter(logfile, fieldnames=fieldnames)
                writer.writeheader()
        with open(self.path, mode='a') as logfile:
            fieldnames = logs.keys()
            writer = csv.DictWriter(logfile, fieldnames=fieldnames)
            writer.writerow(logs)
