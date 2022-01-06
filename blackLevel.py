'''
黑电平矫正异常：1.将RGB图像转换为RAW单通道图像；2.改变图像的G、R通道，使得图像偏绿或者偏红
'''
import random

import cv2
import numpy as np
from RGB2RAW import RGB2Bayer_RG

def black_level_correct_more(img, color_num=255):
    '''模拟黑电平校正过多，图像变绿'''
    # 生成蒙版，改变图像整体颜色
    mask = np.zeros(img.shape, img.dtype)
    mask[:, :, 1] = color_num
    dst = cv2.addWeighted(img, 0.7, mask, 0.3, 0)
    return dst

def black_level_correct_less(img, color_num=255):
    '''模拟黑电平校正较少，图像变红'''
    # 生成蒙版，改变图像整体颜色
    mask = np.zeros(img.shape, img.dtype)
    mask[:, :, 2] = color_num
    dst = cv2.addWeighted(img, 0.7, mask, 0.3, 0)
    return dst

# '''
#下面几行代码用来验证增强结果
ori_img = cv2.imread("../VOCdevkit/VOC2007/JPEGImages/000000.jpg")
# cv2.imshow('original img', ori_img)
black_src = black_level_correct_less(ori_img)
cv2.imshow('black img', black_src)
cv2.waitKey(0)
# '''
