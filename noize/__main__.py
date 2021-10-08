import argparse
from noize import __version__
from noize.noise import cmd_sp


CMD_SP = "salt-and-pepper"


def parse_args(args: argparse.Namespace):
    if args.command == CMD_SP:
        cmd_sp(args.img, args.probability, args.output)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Apply noise to images."
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version = f"{parser.prog} version {__version__}"
    )
    subparsers = parser.add_subparsers(help="Apply different kind of noise algorithms.")

    parser_sp = subparsers.add_parser(CMD_SP, help="Apply salt and pepper noise.")
    parser_sp.add_argument(
        "img", type=str,
        metavar="<file>", help="Source image file."
    )
    parser_sp.add_argument(
        "-o", "--output", type=str, default="output.png",
        metavar="<file>", help="Output file."
    )
    parser_sp.add_argument(
        "-p", "--probability", type=float, default=0.1,
        help="Probability of the noise. Default 0.1"
    )
    parser_sp.set_defaults(command=CMD_SP)
    args = parser.parse_args()
    parse_args(args)




if __name__ == "__main__":
    main()
