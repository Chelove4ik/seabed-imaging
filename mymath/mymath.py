import math

import numpy
from PIL import Image, ImageDraw
from numba import njit


def function43(test, arr):
    image = Image.new("RGB", (arr.shape[1], arr.shape[0]))
    height = image.size[1]
    width = image.size[0]
    draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
    for x in range(height):
        for y in range(width):
            try:
                1 / arr[x][y]
                sr = int((255 * math.log(round((test - 1) / arr[x][y] + 1), int(test))))
                draw.point((y, x), (sr, sr, sr))
            except Exception:
                sr = int(0.4)
                draw.point((y, x), (sr, sr, sr))
    return image


def function364(ld, mu, arr):
    height = arr.shape[0]
    width = arr.shape[1]
    c = 1500
    ji = 1
    li = c * 0.4 / 2

    @njit(fastmath=True, parallel=True)
    def calc364():
        sr_arr = numpy.zeros(arr.shape)
        for x in range(height):
            for y in range(width):
                if arr[x][y] != 0:
                    sr = int((2 * math.pi * li * li) / (c * ji) * math.sqrt(li * li - ld * ld) * arr[x][y] * math.exp(
                        2 * mu * li) / 1_000_000_000)
                else:
                    sr = int(0.4)
                sr_arr[x, y] = sr
        return sr_arr

    arr_sr = calc364()

    print('done calc')

    image = Image.fromarray(arr_sr, 'I')
    image = image.convert('RGB')
    return image
