import argparse
import numpy as np
from PIL import Image
from noize.noise import exponential, salt_and_pepper, rayleigh, gaussian, erlang, periodic


CMD_PER = "periodic"
CMD_SP = "salt-and-pepper"
CMD_GSS = "gaussian"
CMD_RAY = "rayleigh"
CMD_ER = "erlang"
CMD_EXP = "exponential"
CMD_UNF = "uniform"


def apply_cmd(args: argparse.Namespace) -> None:
    img = Image.open(args.img)

    if args.command == CMD_PER:
        noisy_im = periodic(np.array(img), args.mode, args.angle, args.wavelength)
    elif args.command == CMD_SP:
        noisy_im = salt_and_pepper(np.array(img), args.probability, args.seed)
    elif args.command == CMD_GSS:
        noisy_im = gaussian(np.array(img), args.mean, args.var, args.seed)
    elif args.command == CMD_RAY:
        noisy_im = rayleigh(np.array(img), args.loc, args.scale, args.seed)
    elif args.command == CMD_ER:
        noisy_im = erlang(np.array(img), args.a, args.loc, args.scale, args.seed)
    elif args.command == CMD_EXP:
        noisy_im = exponential(np.array(img), args.loc, args.scale, args.seed)
    elif args.command == CMD_UNF:
        noisy_im = exponential(np.array(img), args.loc, args.scale, args.seed)

    noisy_im = Image.fromarray(noisy_im)
    noisy_im.save(args.output)
