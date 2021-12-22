## A simple solution for serving an easyocr text recognition model
Test task: https://github.com/xbodx/ds-task-junior/blob/main/README.md

This implementation uses a pretrained easyocr model

https://www.jaided.ai/easyocr/

Served with flask and waitress

### Setup

 - Install pytorch following instructions in the link below:

https://pytorch.org/get-started/locally/

In order to use GPU, make sure that your pytorch and cuda versions are compatible.
Using GPU is highly recommended.

To set up prerequisites execute in bash:
```bash
pip install -r requirements.txt
```
macos users (additional step required):
```bash
brew install libomp
```
### Usage

To launch the script for russian/english text recognition execute in bash:
```bash
python main.py
```
For other languages' text recognition list those languages as shown below:
```bash
python main.py --languages ch_sim en ru 
```
If any of listed languages are not supported they'll be defaulted to ru/en.

Complete list of supported languages can be found here:

https://www.jaided.ai/easyocr/

Script's functionality can be checked be sending a post request with a random picture to localhost on 5000 port.
Example:
```
import requests
import base64
import json

with open("test.jpg", "rb") as img:
    img = base64.b64encode(img.read())
response = requests.post("http://localhost:5000/text-recognition", data={"img":img})
print(response.json())
```
This code will return a list with recognized texts.
```
import requests
import base64
import json

with open("test.jpg", "rb") as img:
    img = base64.b64encode(img.read())
response = requests.post("http://localhost:5000/text-recognition", data={"img":"mock data"})
print(response.json())
```
This code will return a 400, "Bad request" in case request contents are not a base64 encoded picture
