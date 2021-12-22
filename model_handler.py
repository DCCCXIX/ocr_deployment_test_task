import base64
import io
import logging

import easyocr
import torch
from PIL import Image


class Model_Handler:
    def __init__(self, langs):
        self.device = torch.device("cpu") if not torch.cuda.is_available() else torch.device("cuda:0")
        logging.info(f"Running on {self.device}")
        logging.info(f"Recognition for languages: {langs}")

        self.model = easyocr.Reader(langs, gpu=True if self.device.type == "cuda" else False)

    def predict(self, img):
        try:
            img = base64.b64decode(img)
            img = Image.open(io.BytesIO(img))
            result = self.model.readtext(img, detail=0)
        except Exception:
            logging.exception("Failed to proccess input")
            result = []
        return result
