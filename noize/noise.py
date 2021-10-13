import numpy as np
from scipy import stats
from noize import util


def __periodic_noise(im, angle, wavelength):
    x = np.arange(0, im.shape[0])
    y = np.arange(0, im.shape[1])
    xv, yv = np.meshgrid(x, y)
    noise = np.sin(2*np.pi*(xv*np.cos(angle) + yv*np.sin(angle))/wavelength)
    # scale to [0,1]
    noise_scaled = util.scale_noise(noise)
    noise_im = (im + noise_scaled)/2
    return noise_im


def periodic(image, mode, angle, wavelength):
    util.check_input(image, accepted_shapes=("gray", "RGB"))
    im_arr = image/255.0
    if mode == "gray":
        if len(im_arr.shape) == 3:
            im_arr = np.average(im_arr, weights=[0.299, 0.587, 0.114], axis=2)
        noise_im = __periodic_noise(im_arr, angle, wavelength)
        return (noise_im*255).astype(np.uint8)

    util.check_input(image, accepted_shapes=("RGB"))
    if mode == "R":
        noise_im = im_arr.copy()
        noise_im[:, :, 0] = __periodic_noise(noise_im[:, :, 0], angle, wavelength)
    elif mode == "G":
        noise_im = im_arr.copy()
        noise_im[:, :, 1] = __periodic_noise(noise_im[:, :, 1], angle, wavelength)
    elif mode == "B":
        noise_im = im_arr.copy()
        noise_im[:, :, 2] = __periodic_noise(noise_im[:, :, 2], angle, wavelength)
    elif mode == "+":
        noise_im = im_arr.copy()
        for i in range(3):
            noise_im[:, :, i] = __periodic_noise(noise_im[:, :, i], angle, wavelength)
    else:
        raise util.BadModeException("Bad mode {}.".format(mode))
    return (noise_im*255).astype(np.uint8)


def salt_and_pepper(image, prob, seed=None):
    """Apply salt and pepper noise to given grayscale or rgb image with given prob."""
    util.check_input(image)
    output = image.copy()
    rng = np.random.default_rng(seed)

    def sp(im, prob, rng):
        probs = rng.random(im.shape[:2])
        im[probs < (prob / 2)] = 0
        im[probs > 1 - (prob / 2)] = 255
        return im

    if len(image.shape) == 2:
        output = sp(output, prob, rng)
    elif len(image.shape) == 3:
        for i in range(image.shape[2]):
            output[:, :, i] = sp(output[:, :, i], prob, rng)
    return output.astype(np.uint8)


def gaussian(image, mean, var, seed=None):
    rng = np.random.default_rng(seed)
    return __noise_with_pdf(image, rng.normal, loc=mean, scale=var**0.5)


def rayleigh(image, loc, scale, seed):
    return __noise_with_pdf(image, stats.rayleigh.rvs, loc=loc, scale=scale, random_state=seed)


def erlang(image, a, loc, scale, seed):
    return __noise_with_pdf(image, stats.gamma.rvs, a=a, loc=loc, scale=scale, random_state=seed)


def exponential(image, loc, scale, seed):
    return __noise_with_pdf(image, stats.expon.rvs, loc=loc, scale=scale, random_state=seed)


def uniform(image, loc, scale, seed):
    return __noise_with_pdf(image, stats.uniform.rvs, loc=loc, scale=scale, random_state=seed)


def __noise_with_pdf(im_arr, pdf, **kwargs):
    util.check_input(im_arr)
    im_arr = im_arr/255.0
    noise = pdf(**kwargs, size=im_arr.shape)
    out_im = im_arr + noise
    out_im = np.clip(out_im, 0.0, 1.0)
    return (out_im*255.0).astype(np.uint8)
