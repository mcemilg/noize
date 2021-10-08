import cv2
import numpy as np
from PIL import Image


def cmd_sp(img_path, prob, output_path):
    img = Image.open(img_path)
    noisy_im_arr = salt_and_pepper(np.array(img), prob)
    noisy_im = Image.fromarray(noisy_im_arr) 
    noisy_im.save(output_path)


def salt_and_pepper(image, prob):
    """Apply salt and pepper noise to given grayscale or rgb image with given prob."""
    output = image.copy()

    def sp(im, prob):
        probs = np.random.random(im.shape[:2])
        im[probs < (prob / 2)] = 0
        im[probs > 1 - (prob / 2)] = 255
        return im

    if len(image.shape) == 2:
        output = sp(output, prob)
    else:
        channels = image.shape[2]
        output = np.array(cv2.split(output))
        for im in output:
            sp(im, prob)
        output = np.array(cv2.merge(output))
    return output