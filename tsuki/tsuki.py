# -*- coding: utf-8 -*- #
import sys

import emoji
import numpy as np
from PIL import Image


def draw(path: str, col: int = 50) -> None:

    tsuki_matrixs = load_tsuki_matrixs()
    img = preprocess(path, col)

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


def load_tsuki_matrixs():
    """
    月行列を返す関数

    Args:
        無し
    Return:
        月行列8個, (numpyの行列のリスト)
    """
    tsuki_0 = np.matrix([[-1, -1, -1, -1],
                        [-1, -1, -1, -1],
                        [-1, -1, -1, -1],
                        [-1, -1, -1, -1]])

    tsuki_1 = np.matrix([[-1, -1, -1, 1],
                        [-1, -1, -1, 1],
                        [-1, -1, -1, 1],
                        [-1, -1, -1, 1]])

    tsuki_2 = np.matrix([[-1, -1, 1, 1],
                        [-1, -1, 1, 1],
                        [-1, -1, 1, 1],
                        [-1, -1, 1, 1]])

    tsuki_3 = np.matrix([[-1, 1, 1, 1],
                        [-1, 1, 1, 1],
                        [-1, 1, 1, 1],
                        [-1, 1, 1, 1]])

    tsuki_4 = np.matrix([[1, -1, -1, -1],
                        [1, -1, -1, -1],
                        [1, -1, -1, -1],
                        [1, -1, -1, -1]])

    tsuki_5 = np.matrix([[1, 1, -1, -1],
                        [1, 1, -1, -1],
                        [1, 1, -1, -1],
                        [1, 1, -1, -1]])

    tsuki_6 = np.matrix([[1, 1, 1, -1],
                        [1, 1, 1, -1],
                        [1, 1, 1, -1],
                        [1, 1, 1, -1]])

    tsuki_7 = np.matrix([[1, 1, 1, 1],
                        [1, 1, 1, 1],
                        [1, 1, 1, 1],
                        [1, 1, 1, 1]])

    return [tsuki_0, tsuki_1, tsuki_2, tsuki_3,
            tsuki_4, tsuki_5, tsuki_6, tsuki_7]


def index2tsuki(index):
    """
    indexから絵文字対応する絵文字を返す関数
    Args:
        index
    Return:
        絵文字
    """
    if index==0:
        return emoji.emojize(':new_moon:')
    if index==1:
        return emoji.emojize(':waxing_crescent_moon:')
    if index==2:
        return emoji.emojize(':first_quarter_moon:')
    if index==3:
        return emoji.emojize(':waxing_gibbous_moon:')
    if index==4:
        return emoji.emojize(':waning_crescent_moon:')
    if index==5:
        return emoji.emojize(':last_quarter_moon:')
    if index==6:
        return emoji.emojize(':waning_gibbous_moon:')
    else:
        return emoji.emojize(':full_moon:')


def preprocess(path, col):
    """
    画像の前処理。グレスケール、画質下げ、その他前処理。
    Args:
        path: 画像のパス
        col: 月の列の数
    Return:
        img: 前処理が完了したnumpyの行列
    """
    img = Image.open(path)
    img = img.convert('L')

    width = col*4
    height = int(width*(img.height/img.width))
    height -= height%4

    img = img.resize((width, height))
    img = np.matrix(img)
    img = (img/128.) - 1.

    return img
