import random

import cv2
import numpy as np
from RGB2RAW import RGB2Bayer_RG

def black_level_correct_more(img, color_num=255):
    #E-BLC
    mask = np.zeros(img.shape, img.dtype)
    mask[:, :, 1] = color_num
    dst = cv2.addWeighted(img, 0.7, mask, 0.3, 0)
    return dst

def black_level_correct_less(img, color_num=255):
    #I-BLC
    mask = np.zeros(img.shape, img.dtype)
    mask[:, :, 2] = color_num
    dst = cv2.addWeighted(img, 0.7, mask, 0.3, 0)
    return dst

# '''
#test
ori_img = cv2.imread("../VOCdevkit/VOC2007/JPEGImages/000000.jpg")
# cv2.imshow('original img', ori_img)
black_src = black_level_correct_less(ori_img)
cv2.imshow('black img', black_src)
cv2.waitKey(0)
# '''
