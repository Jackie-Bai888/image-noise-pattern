import numpy as np
import cv2


def RGB2Bayer_RG(img):
    
    row, col, chl = img.shape
    ext_x, ext_y = row % 4, col % 4
    img = img[0:row - ext_x, 0:col - ext_y, :]
    row, col, chl = img.shape
    img[0:row:2, 0:col:2, 0:2] = 0, 0  #R
    img[0:row:2, 1:col:2, [0, 2]] = 0, 0  #G
    img[1:row:2, 0:col:2, [0, 2]] = 0, 0  #G
    img[1:row:2, 1:col:2, 1:3] = 0, 0  #B

    raw = np.zeros((row, col), dtype=np.uint8)
    raw[0:row:2, 0:col:2] = img[0:row:2, 0:col:2, 2]  # red
    raw[0:row:2, 1:col:2] = img[0:row:2, 1:col:2, 1]  # green
    raw[1:row:2, 0:col:2] = img[1:row:2, 0:col:2, 1]  # green
    raw[1:row:2, 1:col:2] = img[1:row:2, 1:col:2, 0]  # blue
    # raw.tofile('cvt_RG.raw')  # 8bit
    return raw


'''
#test
src = cv2.imread("../VOCdevkit/VOC2007/JPEGImages/000000.jpg")
raw_image = RGB2Bayer_RG(src)
cv2.imshow('raw image', raw_image)
cv2.waitKey(0)
'''
