import numpy as np
import cv2
import random


def color_correction_error(img):
    fImg = img.astype(np.float32)
    fImg = fImg / 255.0
    #
    hlsImg = cv2.cvtColor(fImg, cv2.COLOR_BGR2HLS)
    s = int(random.uniform(-30, 100))
    MAX_VALUE = 100
    lsImg = np.zeros(img.shape, np.float32)
    hlsImg[:, :, 2] = (1.0 + s / float(MAX_VALUE)) * hlsImg[:, :, 2]
    hlsImg[:, :, 2][hlsImg[:, :, 2] > 1] = 1
    # hlsImg[:, :, 2] -= s
    # HLS2BGR
    lsImg = cv2.cvtColor(hlsImg, cv2.COLOR_HLS2BGR)
    lsImg[:, :, :] = lsImg[:, :, :] * 255
    lsImg = lsImg.astype(np.uint8)
    return lsImg


# '''
#test
src = cv2.imread("../VOCdevkit/VOC2007/JPEGImages/000000.jpg")
cv2.imshow('original img', src)
black_src = color_correction_error(src)
cv2.imshow('color img', black_src)
cv2.waitKey(0)
# '''
