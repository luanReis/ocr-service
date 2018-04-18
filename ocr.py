from PIL import Image

import pytesseract
import argparse
import cv2
import os


def _apply_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def _apply_thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

def _apply_blurring(image):
    return cv2.medianBlur(image, 3)

def preprocess(image, type):
    grayscale_image = _apply_grayscale(image)

    if type == "thresh": return _apply_thresholding(grayscale_image)
    elif type == "blur": return _apply_blurring(grayscale_image)

    return grayscale_image

def read_from_disk(filename):
    return cv2.imread(filename)

def save_to_disk(image):
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, image)
    return filename

def remove_from_disk(filename):
    os.remove(filename)

def extract_text(filename):
    return pytesseract.image_to_string(Image.open(filename))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--image",
        required=True,
        help="path to input image to be OCR'd")

    parser.add_argument(
        "-p",
        "--preprocess",
        type=str,
        default="thresh",
        help="type of preprocessing to be done")

    args = parser.parse_args()

    image = read_from_disk(args.image)
    preprocessed_image = preprocess(image, args.preprocess)

    temp_file = save_to_disk(preprocessed_image)

    print(extract_text(temp_file))

    remove_from_disk(temp_file)
