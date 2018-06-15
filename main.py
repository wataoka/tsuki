# -*- coding: utf-8 -*- #

import sys
import numpy as np
from PIL import Image

from utils import load_tsuki_matrix, preprocess, index2tsuki

IMAGE_URL = "./images/wataoka.jpeg"


if __name__ == "__main__":
    tsuki_matrixs = load_tsuki_matrix()
    img = preprocess(IMAGE_URL)

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

