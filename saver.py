import json
import sys
import time
import torch

class Saver:

    def __init__(self, model):

        assert len(sys.argv) > 1

        self.path = None
        for arg in sys.argv:
            if "--config=" in arg:
                firstsplit = arg.split("=")[1]
                index = firstsplit.rfind("/")
                self.path = firstsplit[:index] + "/model.pt"
                break

        assert self.path is not None

        self.model = model

    def save(self):
        torch.save(self.model, self.path)
