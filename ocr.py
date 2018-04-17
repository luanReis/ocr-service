from PIL import Image

import pytesseract
import argparse


def extract_text(filename):
    return pytesseract.image_to_string(Image.open(filename))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--image",
        required=True,
        help="path to input image to be OCR'd")

    args = parser.parse_args()

    print(extract_text(args.image))
