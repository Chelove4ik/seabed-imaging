import string
import cv2

def ifile(path : string):
    oarr = []
    with open(path,'r') as data_file:
        for line in data_file:
            data = line.split()
            oarr.append(data)
    return oarr

def ofile(path, img):
    isSaved = cv2.imwrite(path, img)

    if isSaved:
        print('Image is successfully saved')
    else:
        print('Something gone wrong')