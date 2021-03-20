#!/usr/bin/env python

import argparse
import random
import os
import sys


def hanky_pass():
    parser = argparse.ArgumentParser(prog=sys.argv[0], description="Generate a Hankified password")
    parser.add_argument(
        "--word-file",
        "-f",
        metavar="<FILENAME>",
        help="Path to a list of words",
        default=os.path.join(os.path.dirname(__file__), "words.txt"),
        required=False,
    )
    parser.add_argument(
        "--num-words",
        "-n",
        metavar="<NUMBER OF WORDS>",
        default=4,
        type=int,
        help="Number of words in a password (default: 4)",
        required=False,
    )
    args = parser.parse_args()

    pw = []

    if not os.path.isfile(args.word_file):
        print(f"ERROR: {args.word_file} does not exist or is not a file")
        exit(1)

    if args.num_words < 3 or args.num_words > 6:
        print("ERROR: --num-words must be between 3 and 6")
        exit(1)

    with open(args.word_file, "r") as fd:
        contents = fd.read()

    words = contents.split("\n")

    for i in range(args.num_words):
        while True:
            word = random.choice(words)
            if len(word) > 2 and len(word) < 10 and word not in pw:
                pw.append(word.capitalize())
                break

    print(f"{''.join(pw)}{random.randint(-1, 100):02}")


if __name__ == "__main__":
    hanky_pass()