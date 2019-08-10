import json
import sys

class Logger:

    def __init__(self):

        assert len(sys.argv) > 1

        self.path = None
        for arg in sys.argv:
            if "--config=" in arg:
                firstsplit = arg.split("=")[1]
                index = firstsplit.rfind("/")
                self.path = firstsplit[:index] + "logs.json" #LOOK AT NAMING
                break

        assert self.path is not None
        #print("The path is: " + self.path)
