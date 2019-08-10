import os
import sys
import json

class Args:

    def __init__(self):

        assert len(sys.argv) > 1

        path = None
        for arg in sys.argv:
            if "--config=" in arg:
                path = arg.split("=")[1]
                break

        assert path is not None

        with open(path) as json_file:
            conf = json.load(json_file)
            self.conf = conf
            for name, value in conf.items():
                setattr(self, name, value)
