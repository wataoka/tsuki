# -*- coding: utf-8 -*- #
import argparse

import tsuki


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", default="./images/apple.png", type=str)
    parser.add_argument("--col", default=30, type=int)
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    tsuki.draw(args.path, args.col)

if __name__ == "__main__":
    main()
