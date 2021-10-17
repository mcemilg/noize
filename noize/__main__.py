import sys
import argparse
from noize import __version__
from noize.cmd import CMD_EXP, CMD_PER, CMD_UNF, CMD_SP, CMD_RAY, CMD_GSS, CMD_ER, apply_cmd


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Apply noise to images."
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version=f"{parser.prog} version {__version__}"
    )
    subparsers = parser.add_subparsers(help="Apply different kind of noise algorithms.")

    # periodic
    subparser = subparsers.add_parser(CMD_PER, help="Apply periodic noise.")
    subparser.add_argument(
        "img", type=str,
        metavar="<file>", help="Source image file."
    )
    subparser.add_argument(
        "-o", "--output", type=str, default="output.png",
        metavar="<file>", help="Output file."
    )
    subparser.add_argument(
        "-m", "--mode", type=str, default="gray",
        help="Apply noise to gray, specific channel or all channels."
             " Options: ['gray', 'R', 'G', 'B', '+']. Default 'gray'."
    )
    subparser.add_argument(
        "-a", "--angle", type=float, default=0.0,
        help="Angle of the wave. Default 0.0"
    )
    subparser.add_argument(
        "-w", "--wavelength", type=float, default=100.0,
        help="Length of the wave. Default 100.0"
    )
    subparser.set_defaults(command=CMD_PER)

    # salt and pepper
    subparser = subparsers.add_parser(CMD_SP, help="Apply salt and pepper noise.")
    subparser.add_argument(
        "img", type=str,
        metavar="<file>", help="Source image file."
    )
    subparser.add_argument(
        "-o", "--output", type=str, default="output.png",
        metavar="<file>", help="Output file."
    )
    subparser.add_argument(
        "-p", "--probability", type=float, default=0.1,
        help="Probability of the noise. Default 0.1"
    )
    subparser.add_argument(
        "--seed", type=int, default=None,
        help="Seed value, default None."
    )
    subparser.set_defaults(command=CMD_SP)

    # gaussian
    subparser = subparsers.add_parser(CMD_GSS, help="Apply gaussian noise.")
    subparser.add_argument(
        "img", type=str,
        metavar="<file>", help="Source image file."
    )
    subparser.add_argument(
        "-o", "--output", type=str, default="output.png",
        metavar="<file>", help="Output file."
    )
    subparser.add_argument(
        "-m", "--mean", type=float, default=0.0,
        help="Mean of the distribution. Default 0.0"
    )
    subparser.add_argument(
        "-v", "--var", type=float, default=0.01,
        help="Variance of the distribution. Default 0.01"
    )
    subparser.add_argument(
        "--seed", type=int, default=None,
        help="Seed value, default None."
    )
    subparser.set_defaults(command=CMD_GSS)

    # rayleigh
    subparser = subparsers.add_parser(CMD_RAY, help="Apply rayleigh noise.")
    subparser.add_argument(
        "img", type=str,
        metavar="<file>", help="Source image file."
    )
    subparser.add_argument(
        "-o", "--output", type=str, default="output.png",
        metavar="<file>", help="Output file."
    )
    subparser.add_argument(
        "-l", "--loc", type=float, default=0.0,
        help="Loc (center) of the distribution. Default 0.0"
    )
    subparser.add_argument(
        "-s", "--scale", type=float, default=0.1,
        help="Scale of the distribution. Default 0.1"
    )
    subparser.add_argument(
        "--seed", type=int, default=None,
        help="Seed value, default None."
    )
    subparser.set_defaults(command=CMD_RAY)

    # erlang
    subparser = subparsers.add_parser(CMD_ER, help="Apply erlang (gamma) noise.")
    subparser.add_argument(
        "img", type=str,
        metavar="<file>", help="Source image file."
    )
    subparser.add_argument(
        "-o", "--output", type=str, default="output.png",
        metavar="<file>", help="Output file."
    )
    subparser.add_argument(
        "-a", type=int, default=1,
        help="Shape parameter for erlang, default 1. Check scipy.stats.gamma for reference."
    )
    subparser.add_argument(
        "-l", "--loc", type=float, default=0.0,
        help="Loc (center) of the distribution. Default 0.0"
    )
    subparser.add_argument(
        "-s", "--scale", type=float, default=0.1,
        help="Scale of the distribution. Default 0.1"
    )
    subparser.add_argument(
        "--seed", type=int, default=None,
        help="Seed value, default None."
    )
    subparser.set_defaults(command=CMD_ER)

    # exponential
    subparser = subparsers.add_parser(CMD_EXP, help="Apply exponential noise.")
    subparser.add_argument(
        "img", type=str,
        metavar="<file>", help="Source image file."
    )
    subparser.add_argument(
        "-o", "--output", type=str, default="output.png",
        metavar="<file>", help="Output file."
    )
    subparser.add_argument(
        "-l", "--loc", type=float, default=0.0,
        help="Loc (center) of the distribution. Default 0.0"
    )
    subparser.add_argument(
        "-s", "--scale", type=float, default=0.1,
        help="Scale of the distribution. Default 0.1"
    )
    subparser.add_argument(
        "--seed", type=int, default=None,
        help="Seed value, default None."
    )
    subparser.set_defaults(command=CMD_EXP)

    # uniform
    subparser = subparsers.add_parser(CMD_UNF, help="Apply uniform noise.")
    subparser.add_argument(
        "img", type=str,
        metavar="<file>", help="Source image file."
    )
    subparser.add_argument(
        "-o", "--output", type=str, default="output.png",
        metavar="<file>", help="Output file."
    )
    subparser.add_argument(
        "-l", "--loc", type=float, default=0.0,
        help="Loc (center) of the distribution. Default 0.0"
    )
    subparser.add_argument(
        "-s", "--scale", type=float, default=1.0,
        help="Scale of the distribution. Default 1.0"
    )
    subparser.add_argument(
        "--seed", type=int, default=None,
        help="Seed value, default None."
    )
    subparser.set_defaults(command=CMD_UNF)

    args = parser.parse_args()
    if "command" not in args:
        sys.exit("Unknown command.")
    if "img" not in args:
        sys.exit("Input image not given.")
    apply_cmd(args)


if __name__ == "__main__":
    main()
