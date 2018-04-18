from PIL import Image

import pytesseract
import argparse
import cv2
import os


def generate_grayscale_image(image_path):
    image = cv2.imread(image_path)
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale_image

def preprocess_image(image):
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, image)
    return filename

def cleanup(preprocessed_image):
    os.remove(preprocessed_image)

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
    preprocessed_image = preprocess_image(grayscale_image)

    print(extract_text(preprocessed_image))

    cleanup(preprocessed_image)
