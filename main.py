# -*- coding: utf-8 -*- #

import sys
import argparse
import numpy as np

from utils import load_tsuki_matrixs, preprocess, index2tsuki



IMAGE_URL = "./images/wataoka.jpeg"

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", default="./images/apple.png", type=str)
    parser.add_argument("--col", default="50", type=int)
    args = parser.parse_args()

    tsuki_matrixs = load_tsuki_matrixs()
    img = preprocess(args.path, args.col)

    tsuki_list = []

    for i in range(int(np.shape(img)[0]/4)):
        for j in range(int(np.shape(img)[1]/4)):
            row = 4*i
            col = 4*j
            max = -10000
            max_tk = 0
            for n, tk in enumerate(tsuki_matrixs):
                hadamard = np.multiply(img[row:row+4, col:col+4], tk)
                if max < hadamard.sum():
                    max_index = n
                    max = hadamard.sum()
            tsuki_list.append(index2tsuki(max_index))
        tsuki_list.append('\n')

    for i in tsuki_list:
        sys.stdout.write(i)
