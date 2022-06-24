import string

import cv2
import numpy as np


def read_file(path: string):
    arr = []
    with open(path, 'r') as data_file:
        for line in data_file:
            arr.append(list(map(float, line.split())))

    np_array = np.array(arr, dtype=np.float64)
    return np_array


def write_file(path, img):
    is_saved = cv2.imwrite(path, img)

    if is_saved:
        print('Image is successfully saved')
    else:
        print('Something gone wrong')
