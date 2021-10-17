# noize.noise
<a id="noise"></a>

* [noise](#noise)
  * [periodic](#noise.periodic)
  * [salt\_and\_pepper](#noise.salt_and_pepper)
  * [gaussian](#noise.gaussian)
  * [rayleigh](#noise.rayleigh)
  * [erlang](#noise.erlang)
  * [exponential](#noise.exponential)
  * [uniform](#noise.uniform)



<a id="noise.periodic"></a>

# periodic

```python
def periodic(image: np.ndarray, mode: str = "gray", angle: int = 0, wavelength: int = 100) -> np.ndarray
```

Applies periodic noise to given image.

Parameters
----------
image : np.ndarray
    The image which the noise will be added. It can be gray or RGB image.
mode : str, optional
    The mode defines noise channel to be applied. It can be "gray", "R", "G" or "+" which
    applies noise to all RGB channels. All modes expect RGB images expect "gray" which can be
    used with both gray and RGB images. If the mode is "gray" and image is RGB the output will
    be gray. (Default "gray")
angle : int, optional
    The angle of the periodic noise. (Default 0).
wavelength : int, optional
    The wavelength of the periodic (sinusoidal) noise. (Default 100).

Raises
------
noize.util.BadModeException
    If the mode not given properly.
noize.util.BadShapeException
    If the shape is not proper.

Returns
-------
np.ndarray
    The noise applied image. It will be in same shape with the input image unless the mode
    is "gray" and the given image is RGB.

<a id="noise.salt_and_pepper"></a>

# salt\_and\_pepper

```python
def salt_and_pepper(image: np.ndarray, prob: float = 0.1, seed: int = None) -> np.ndarray
```

Apply salt and pepper noise to given grayscale or rgb image with given prob.

Parameters
----------
image : np.ndarray
    The image which the noise will be added. It can be gray, RGB or with multiple channels.
    The noise will be applied to all channels seperately.
prob : float, optional
    The probablity that sp noise to apply. Default 0.1
seed : int, optional
    Seed to be used while adding noise randomly. Default None.

Raises
------
noize.util.BadShapeException
    If the shape is not proper.

Returns
-------
np.ndarray
    The noise applied image. It will be in same shape with the input image.

<a id="noise.gaussian"></a>

# gaussian

```python
def gaussian(image: np.ndarray, mean: float = 0.0, var: float = 0.01, seed: int = None) -> np.ndarray
```

Apply gaussian noise to given grayscale or rgb image.

For the gaussian random generator numpy.random.random function used.

Parameters
----------
image : np.ndarray
    The image which the noise will be added. It can be gray, RGB or with multiple channels.
mean : float, optional
    The mean of the distribution. Default 0.0
var : float, optional
    The variance of the distribution. Default 0.01
seed : int, optional
    Seed to be used while adding noise randomly. Default None.

Raises
------
noize.util.BadShapeException
    If the shape is not proper.

Returns
-------
np.ndarray
    The noise applied image. It will be in same shape with the input image.

<a id="noise.rayleigh"></a>

# rayleigh

```python
def rayleigh(image: np.ndarray, loc: float = 0.0, scale: float = 0.1, seed: int = None) -> np.ndarray
```

Apply rayleigh noise to given grayscale or rgb image.

Check scipy.stats.rayleigh for more information.

Parameters
----------
image : np.ndarray
    The image which the noise will be added. It can be gray, RGB or with multiple channels.
loc : float, optional
    Loc (center) of the distribution. Default 0.0
scale : float, optional
    Scale of the distribution. Default 0.1
seed : int, optional
    Seed to be used while adding noise randomly. Default None.

Raises
------
noize.util.BadShapeException
    If the shape is not proper.

Returns
-------
np.ndarray
    The noise applied image. It will be in same shape with the input image.

<a id="noise.erlang"></a>

# erlang

```python
def erlang(image: np.ndarray, a: int, loc: float, scale: float, seed: int = None) -> np.ndarray
```

Apply erlang (gamma) noise to given grayscale or rgb image.

Check scipy.stats.gamma for more information.

Parameters
----------
image : np.ndarray
    The image which the noise will be added. It can be gray, RGB or with multiple channels.
loc : float, optional
    Loc (center) of the distribution. Default 0.0
scale : float, optional
    Scale of the distribution. Default 0.1
seed : int, optional
    Seed to be used while adding noise randomly. Default None.

Raises
------
noize.util.BadShapeException
    If the shape is not proper.

Returns
-------
np.ndarray
    The noise applied image. It will be in same shape with the input image.

<a id="noise.exponential"></a>

# exponential

```python
def exponential(image: np.ndarray, loc: float, scale: float, seed: int = None) -> np.ndarray
```

Apply exponential noise to given grayscale or rgb image.

Check scipy.stats.expon for more information.

Parameters
----------
image : np.ndarray
    The image which the noise will be added. It can be gray, RGB or with multiple channels.
loc : float, optional
    Loc (center) of the distribution. Default 0.0
scale : float, optional
    Scale of the distribution. Default 0.1
seed : int, optional
    Seed to be used while adding noise randomly. Default None.

Raises
------
noize.util.BadShapeException
    If the shape is not proper.

Returns
-------
np.ndarray
    The noise applied image. It will be in same shape with the input image.

<a id="noise.uniform"></a>

# uniform

```python
def uniform(image: np.ndarray, loc: float, scale: float, seed: int = None) -> np.ndarray
```

Apply uniform noise to given grayscale or rgb image.

Check scipy.stats.uniform for more information.

Parameters
----------
image : np.ndarray
    The image which the noise will be added. It can be gray, RGB or with multiple channels.
loc : float, optional
    Loc (center) of the distribution. Default 0.0
scale : float, optional
    Scale of the distribution. Default 0.1
seed : int, optional
    Seed to be used while adding noise randomly. Default None.

Raises
------
noize.util.BadShapeException
    If the shape is not proper.

Returns
-------
np.ndarray
    The noise applied image. It will be in same shape with the input image.

