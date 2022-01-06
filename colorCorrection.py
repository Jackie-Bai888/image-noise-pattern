import numpy as np
import cv2
import random


def color_correction_error(img):
    """
           #颜色矫正异常
           输入:
               image     图像
           返回颜色矫正异常后的图像
    """
    fImg = img.astype(np.float32)
    fImg = fImg / 255.0
    # 颜色空间转换 BGR转为HLS
    hlsImg = cv2.cvtColor(fImg, cv2.COLOR_BGR2HLS)
    # 随机生成饱和度值
    s = int(random.uniform(-30, 100))
    MAX_VALUE = 100
    # 调整饱和度和亮度后的效果
    lsImg = np.zeros(img.shape, np.float32)
    # 调整饱和度 将hlsImg[:, :, 2]中大于1的全部截取
    hlsImg[:, :, 2] = (1.0 + s / float(MAX_VALUE)) * hlsImg[:, :, 2]
    hlsImg[:, :, 2][hlsImg[:, :, 2] > 1] = 1
    # hlsImg[:, :, 2] -= s
    # HLS2BGR
    lsImg = cv2.cvtColor(hlsImg, cv2.COLOR_HLS2BGR)
    lsImg[:, :, :] = lsImg[:, :, :] * 255
    lsImg = lsImg.astype(np.uint8)
    return lsImg


# '''
#下面几行代码用来验证增强结果
src = cv2.imread("../VOCdevkit/VOC2007/JPEGImages/000000.jpg")
cv2.imshow('original img', src)
black_src = color_correction_error(src)
cv2.imshow('color img', black_src)
cv2.waitKey(0)
# '''
