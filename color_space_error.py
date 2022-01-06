'''
模拟色彩空间转换异常
'''
import random

import cv2
import numpy as np


def color_space_error(img, num_precent = 0.6):
    '''
    模拟色彩空间转换异常
    num_precent : 色彩空间转换异常的像素点
    '''
    # B, G, R = cv2.split(img)
    y_cb_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)#cv2.merge([Y, Cr, Cb])
    Y, Cr, Cb = cv2.split(y_cb_img)
    height, width, _ = img.shape
    num = int(height * width * num_precent)
    pixel_position = random.sample(range(0, height * width), num)
    for pos in pixel_position:
        Y[(pos // width) - 1, pos % width] -= 16  #将转换公式中的常数16去除
        Cr[(pos // width) - 1, pos % width] -= 128 #将转换公式中的常数128去除
        Cb[(pos // width) - 1, pos % width] -= 128 #将转换公式中的常数128去除
    dst = cv2.merge([Y, Cr, Cb])
    output_img = cv2.cvtColor(dst, cv2.COLOR_YCrCb2BGR)
    return output_img

# '''
#下面几行代码用来验证增强结果
src = cv2.imread("../VOCdevkit/VOC2007/JPEGImages/000000.jpg")
cv2.imshow('original img', src)
black_src = color_space_error(src, 0.8)
cv2.imshow('color img1', black_src)
black_src = color_space_error(src, 1)
cv2.imshow('color img2', black_src)
cv2.waitKey(0)
# '''