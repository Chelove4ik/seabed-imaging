import numpy
from PIL import Image, ImageDraw
import math

raws = 1000
columns = 8680


def function43(test, a):
    image = Image.new("RGB", (columns, raws))
    height = image.size[1]
    width = image.size[0]
    draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
    for x in range(height):
        mean = numpy.mean(a[x])
        for y in range(width):
            try:
                1 / a[x][y]
                sr = int((255 * math.log(round((test - 1) / mean + 1), test)))
                draw.point((y, x), (sr, sr, sr))
            except ZeroDivisionError:
                sr = int(0.4)
                draw.point((y, x), (sr, sr, sr))
    return image
    # image.save('test.jpg', "JPEG")
    # image.show()


def function364(li, a):
    image = Image.new("RGB", (columns, raws))
    draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
    height = image.size[1]
    width = image.size[0]
    c = 1500
    mu = 1.8 * 1 / 10 ** 2
    ji = 1
    ld = 12
    li = c * 0.4 / 2
    for x in range(height):
        for y in range(width):
            try:
                1 / a[x][y]
                sr = int((2 * math.pi * li) / (c * ji) * math.sqrt(li * li - ld * ld) * a[x][y] * math.exp(
                    2 * mu * li) / 100000)
                draw.point((y, x), (sr, sr, sr))
            except ZeroDivisionError:
                sr = int(0.4)
                draw.point((y, x), (sr, sr, sr))
    return image
    # image.save('test1.jpg', "JPEG")
    # image.show()


def readFile(path):
    f = open(path, 'r')
    arr = []
    for i in range(raws):
        arr.append([float(n) for n in (f.readline().split())])
    return arr
