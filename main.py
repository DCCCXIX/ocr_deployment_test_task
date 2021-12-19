#!/usr/bin/env python
import os

import cv2
import numpy as np
import waitress
from flask import Flask, request

import model_handler

app = Flask(__name__)


@app.route("/text-recognition", methods=["GET"])
def predict_form_post():
    img = np.fromstring(request.data, np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    return model_handler.mh.predict(img)


if __name__ == "__main__":
    waitress.serve(app, host="0.0.0.0", port=5000)
