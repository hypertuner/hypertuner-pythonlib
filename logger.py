import json
import sys
import time

class Logger:

    def __init__(self):

        assert len(sys.argv) > 1

        self.path = None
        for arg in sys.argv:
            if "--config=" in arg:
                firstsplit = arg.split("=")[1]
                index = firstsplit.rfind("/")
                self.path = firstsplit[:index] + "/logs.json" #LOOK AT NAMING, LOOK AT SLASH
                break

        assert self.path is not None

    def log(self, logs, framenum = time.time()):
        logs["frame"] = framenum
        with open(self.path, 'w') as outfile:
            json.dump(logs, outfile)
