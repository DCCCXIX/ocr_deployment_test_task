import logging

import easyocr
import torch


class Model_Handler:
    def __init__(self):
        self.device = torch.device("cpu") if not torch.cuda.is_available() else torch.device("cuda:0")
        logging.info(f"Running on {'CPU' if not torch.cuda.is_available() else torch.cuda.get_device_name()}")
        self.model = easyocr.Reader(["ru", "en"]).to(self.device)

    def predict(self, img):
        return self.model(img)


mh = Model_Handler()
