import numpy as np
from typing import Tuple


class BadModeException(Exception):
    pass


class BadShapeException(Exception):
    pass


def scale_noise(noise: np.ndarray) -> np.ndarray:
    """scale to [0,1]"""
    return (noise - np.min(noise))/np.ptp(noise)


def check_input(im: np.ndarray, accepted_shapes: Tuple[str]=("gray", "RGB", "custom")) -> None:
    if not isinstance(im, np.ndarray):
        raise BadShapeException("Input should be np.array.")

    im_shape = "unk"
    if len(im.shape) == 2:
        im_shape = "gray"
    elif len(im.shape) == 3 and im.shape[2] == 3:
        im_shape = "RGB"
    elif len(im.shape) == 3:
        im_shape = "custom"
    if im_shape not in accepted_shapes:
        raise BadShapeException("Input shape not proper {}.".format(im.shape))
