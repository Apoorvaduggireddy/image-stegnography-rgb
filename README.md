image stegonography in the context of RGB images involves hiding information within
the pixel values of an image without significantly altering its appearance.
# Image Steganography

A Python tool for hiding and retrieving secret messages or files in images using LSB (Least Significant Bit) steganography.

## Features
- Encode text/files into images
- Decode hidden data from images
- Supports `.png` and `.bmp`
- Optional AES encryption

## Requirements
- Python 3.6+
- Libraries: `Pillow`, `numpy`, `pycryptodome`

## Installation
1. Clone repo:
   ```bash
   git clone https://github.com/your-username/image-steganography.git
   cd image-steganography
2.pip install -r requirements.txt

image-steganography/
├── encode.py
├── decode.py
├── requirements.txt
├── images/
│   ├── cover.png
│   ├── stego.png
├── README.md

