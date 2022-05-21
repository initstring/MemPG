"""
Main module for MemPR

https://github.com/initstring/mempg
MIT License
"""

import sys
import argparse

from mempg import generators


def parse_args():
    """
    Handles user-supplied arguments
    """
    desc = "Generate easy-to-remember passphrases of variables lengths"
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument("-l", "--length", type=int, default=6,
                        help="Length of passphrase to generate. Default: 4")
    parser.add_argument("-n", "--numbers", action="store_true", default=False,
                        help="Add 4 random digits to end. Default: False")
    parser.add_argument("-p", "--phrases", type=int, default=1,
                        help="How many phrases to generate. Default: 1")

    args = parser.parse_args()
    return args


def main():
    """
    Leverages the Generator package to generate a single passphrase
    """
    args = parse_args()
    try:
        generator = generators.Generator(args.length, add_num=args.numbers)
    except ValueError:
        print("[!] I can't count that high, sorry.")
        sys.exit(1)

    print(f"bits of entropy: {generator.entropy}")
    print("-----------------------")

    for _ in range(0, args.phrases):
        generator.make_pass()
        print(generator.phrase)


if __name__ == "__main__":
    main()
