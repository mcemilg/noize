import numpy as np
from noize import util


def test_scale_noise():
    arr = np.arange(-100, 100)
    arr_scaled = util.scale_noise(arr)
    assert arr_scaled.max() <= 1
    assert arr_scaled.min() >= 0
