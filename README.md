## A simple solution for serving an easyocr text recognition model

This implementation uses a pretrained easyocr model for english and russian languages

Served with flask and waitress

### Setup

 - Install pytorch following instructions in the link below:

https://pytorch.org/get-started/locally/

In order to use GPU, make sure that your pytorch and cuda versions are compatible.
Using GPU is adviced.

To set up prerequisites do in bash:
```bash
pip install requirements.txt
```
macos users (additional step):
```bash
brew install libomp
```

### Usage
```bash
python main.py

This will start a flask api that recieves a base64 coded image and returns recognized texts and bounding boxes' coordinates
