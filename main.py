#!/usr/bin/env python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
    datefmt="%m-%d %H:%M",
)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.FileHandler("app.log", "w", "utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-lang",
    "--languages",
    nargs="*",
    default=["en", "ru"],
    type=str,
    help="Languages used for recognition",
    required=False,
)
args = vars(parser.parse_args())

import waitress
from flask import Flask, Response, jsonify, request

import model_handler

app = Flask(__name__)
try:
    mh = model_handler.Model_Handler(langs=args["languages"])
except Exception:
    logging.exception("Languages not supported. Default ru/en languages will be used")
    mh = model_handler.Model_Handler(langs=["en", "ru"])


@app.route("/text-recognition", methods=["POST"])
def predict_form_post():
    try:
        result = mh.predict(request.form["img"])
        return jsonify(result)
    except Exception:
        logging.exception("Bad request")
        return Response("Bad request", status=400)


if __name__ == "__main__":
    waitress.serve(app, host="0.0.0.0", port=5000)
