'''
模拟坏点校正异常：1.将RGB图像转换为RAW单通道图像；2.随机选择RAW图像中的像素点将其像素值设置为0或者1；3.将RAW转换为RGB。
'''
import cv2
import random
from RGB2RAW import RGB2Bayer_RG
import numpy as np

def ori_bad_pixel_error(img, num_precent=0.6):
    """
        #坏点矫正异常:模拟dead pixel，直接将像素点的灰度值变为零
        输入:
        img     图像
        num     坏点数量
        返回坏点矫正异常后的图像
    """
    # 由于在ISP流水线中处于CFA插值异常前，首先将其转变为RAW图像
    raw_img = RGB2Bayer_RG(img)
    height, width = raw_img.shape
    num = int(height * width * num_precent)
    pixel_position = random.sample(range(0, height * width), num)
    for pos in pixel_position:
        raw_img[(pos // width)-1, pos % width] = 0
    # 将RAW图像进行转换RGB图像
    dst = cv2.cvtColor(raw_img, cv2.COLOR_BAYER_BG2BGR)
    return dst
# '''
#下面几行代码用来验证增强结果
src = cv2.imread("../VOCdevkit/VOC2007/JPEGImages/000000.jpg")
bad_img = ori_bad_pixel_error(src, 0.1)
cv2.imshow('bad pixel', bad_img)
cv2.waitKey(0)
# '''

