from PIL import Image

import pytesseract
import argparse
import cv2
import os


def generate_grayscale_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    return filename

def cleanup(temp_file_path):
    os.remove(temp_file_path)

def extract_text(image_path):
    return pytesseract.image_to_string(Image.open(image_path))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--image",
        required=True,
        help="path to input image to be OCR'd")

    args = parser.parse_args()

    image_path = args.image

    grayscale_image = generate_grayscale_image(image_path)
    print(extract_text(grayscale_image))
    cleanup(grayscale_image)
