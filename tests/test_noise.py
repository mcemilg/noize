import pytest
from scipy import stats
import numpy as np
from numpy.testing import assert_array_equal
from noize import util
from noize import noise


def test_mode_periodic():
    """Ensure modes are working properly."""
    angle = 0
    wl = 100
    im_shape = (128, 128, 3)
    im = np.zeros(im_shape)
    nz = noise.periodic(im, "gray", angle, wl)
    assert len(nz.shape) == 2

    nz = noise.periodic(im, "R", angle, wl)
    assert nz[:, :, 0].sum() != 0
    assert nz[:, :, 1].sum() == 0
    assert nz[:, :, 2].sum() == 0

    nz = noise.periodic(im, "G", angle, wl)
    assert nz[:, :, 0].sum() == 0
    assert nz[:, :, 1].sum() != 0
    assert nz[:, :, 2].sum() == 0

    nz = noise.periodic(im, "B", angle, wl)
    assert nz[:, :, 0].sum() == 0
    assert nz[:, :, 1].sum() == 0
    assert nz[:, :, 2].sum() != 0

    nz = noise.periodic(im, "+", angle, wl)
    assert nz[:, :, 0].sum() != 0
    assert nz[:, :, 1].sum() != 0
    assert nz[:, :, 2].sum() != 0

    with pytest.raises(util.BadModeException):
        noise.periodic(im, "QWE", angle, wl)


def test_bad_shape_periodic():
    angle = 0
    wl = 100
    im_shape = (128, 128, 4)
    im = np.zeros(im_shape)
    with pytest.raises(util.BadShapeException):
        noise.periodic(im, "+", angle, wl)

    im_shape = (128, 128)
    im = np.zeros(im_shape)
    with pytest.raises(util.BadShapeException):
        noise.periodic(im, "+", angle, wl)


def test_wavelength_periodic():
    angle = 0
    im_shape = (128, 128)
    im = np.zeros(im_shape)
    nz1 = noise.periodic(im, "gray", angle, 100)
    nz2 = noise.periodic(im, "gray", angle, 200)
    assert nz1.sum() < nz2.sum()


def test_set_seed_sp():
    seed = 25
    im_shape = (128, 128, 3)
    prob = 0.5
    im = np.zeros(im_shape)
    assert_array_equal(
        noise.salt_and_pepper(im, prob, seed),
        noise.salt_and_pepper(im, prob, seed)
    )


def test_edge_probs_sp():
    im_shape = (128, 128, 3)
    im = np.ones(im_shape)

    nz = noise.salt_and_pepper(im, 2.0)
    assert nz.max() == 255 and nz.min() == 255

    nz = noise.salt_and_pepper(im, 0.0)
    assert nz.max() == 1 and nz.min() == 1

    nz = noise.salt_and_pepper(im, 1.0)
    assert 1 in im and 1 not in nz


def test_different_shapes_sp():
    im_shape = (128, 128)
    im = np.ones(im_shape)
    nz = noise.salt_and_pepper(im, 1.0)
    assert 1 not in nz

    im_shape = (128, 128, 2)
    im = np.ones(im_shape)
    nz = noise.salt_and_pepper(im, 1.0)
    assert 1 not in nz

    im_shape = (128, 128, 3)
    im = np.ones(im_shape)
    nz = noise.salt_and_pepper(im, 1.0)
    assert 1 not in nz


def test_sp():
    """Ensure the noise rate similar to given prob."""
    seed = 25
    prob = 0.5
    im_shape = (256, 256)
    im = np.ones(im_shape)
    nz = noise.salt_and_pepper(im, prob, seed=seed)
    noize_count = (nz != 1).sum()
    noize_prob = noize_count/(im_shape[0]*im_shape[1])
    assert (noize_prob - prob) < 1e-2


def test_set_seed_gaussian():
    seed = 25
    im_shape = (128, 128, 3)
    mean = 0.0
    var = 0.01
    im = np.zeros(im_shape)
    assert_array_equal(
        noise.gaussian(im, mean, var, seed),
        noise.gaussian(im, mean, var, seed)
    )


def test_set_seed_pdf():
    seed = 25
    im_shape = (128, 128, 3)
    loc = 0.0
    scale = 0.1
    pdf = stats.rayleigh.rvs
    im = np.zeros(im_shape)
    assert_array_equal(
        noise.__noise_with_pdf(im, pdf, loc=loc, scale=scale, random_state=seed),
        noise.__noise_with_pdf(im, pdf, loc=loc, scale=scale, random_state=seed)
    )


def test_overflow_pdf():
    loc = 0.0
    scale = 10
    im_shape = (128, 128, 3)
    im = np.zeros(im_shape)
    pdf = stats.rayleigh.rvs
    res = noise.__noise_with_pdf(im, pdf, loc=loc, scale=scale)
    assert res.max() <= 255
    assert res.min() >= 0
