# Noize

Noize is a tool and a library to apply different kind of noise methods to images.
Various noises with parameters can be applied for both grayscale and RGB images.

Here is an example, from left to right, original, salt and pepper, gaussian, periodic versions of an image.

<p align="center">
  <img src="https://raw.githubusercontent.com/mcemilg/noize/master/doc/lenna.png" width="22%" />
  <img src="https://raw.githubusercontent.com/mcemilg/noize/master/doc/sp.png" width="22%" /> 
  <img src="https://raw.githubusercontent.com/mcemilg/noize/master/doc/gaussian.png" width="22%" />
  <img src="https://raw.githubusercontent.com/mcemilg/noize/master/doc/periodic.png" width="22%" />
</p>

Noize requiers Python 3.8 or newer versions, however some or all methods can be used older Python 3 versions.

Some supported methods:

- Periodic Noise
- Salt and Pepper Noise
- Noises with Probability Density Functions


## Installation

Install Noize from PyPI:

```shell
$ pip install noize
```


## Cli Usage

Here is an example to apply salt and pepper noise, use `noize --help` for more:

```shell
$ noize salt-and-pepper lenna.png -p 0.01 --seed 25 -o output.png
```

## Lib Usage

```python
import numpy as np
from PIL import Image
from noize import noise

# load image
im = Image.open("doc/lenna.png")

# apply noise (input should be np.ndarray)
out = noise.salt_and_pepper(np.array(im), 0.1, 25)

# save result
out_im = Image.fromarray(out)
out_im.save("output.png")
```

Checkout the noise module [documentation](https://github.com/mcemilg/noize/blob/master/doc/doc.md) for more.


## License

```license
MIT License

Copyright (c) 2021 mcemilg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

