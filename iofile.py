import string

import cv2
import numpy as np


def read_file(path: string):
    arr = []
    with open(path, 'r') as data_file:
        for line in data_file:
            arr.append(list(map(float, line.split())))

    np_array = np.array(arr, dtype=np.float32)
    np_array.tofile(f'{path}.npy')
    return np_array


def fast_read_file(path: string):
    arr = np.fromfile(path, dtype=np.float32)
    arr = arr.reshape((7384, 8680))
    return arr


def write_file(path, img):
    is_saved = cv2.imwrite(path, img)

    if is_saved:
        print('Image is successfully saved')
    else:
        print('Something gone wrong')
