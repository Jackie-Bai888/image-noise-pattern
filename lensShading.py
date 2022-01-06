import cv2
import numpy as np
import math
from RGB2RAW import RGB2Bayer_RG


def lens_shading_error(img, alpha=0.5):
    """
         镜头矫正异常
         输入:
             img  图像
         返回镜头矫正异常后的图像
    """
    # 由于在ISP流水线中处于CFA插值异常前，首先将其转变为RAW图像
    img = RGB2Bayer_RG(img)
    # 获取图像属性
    row, col = img.shape
    # 阴影颜色深度比例矩阵
    shading = np.ones(img.shape)
    # 阴影区域内半径大小
    r = ((max(row, col) - min(row, col))// 2*alpha)
    print(r)
    # 对角线长度一半
    size = math.sqrt((row // 2) ** 2 + (col // 2) ** 2)
    # 镜头中心坐标
    center = (row // 2, col // 2)
    # 1和0控制边缘暗度，暗度随距离镜头中心距离线性变化
    a = 1 / (r - size)
    b = 0 - size * a
    for i in range(row):
        for j in range(col):
            d = math.sqrt((i - center[0]) ** 2 + (j - center[1]) ** 2)  # 与中心距离,欧式距离
            if d <= r:
                # 小于阴影内半径不做处理
                continue
            else:
                # 根据距离计算阴影颜色深度
                scale = a * d + b
                shading[i][j] = shading[i][j] * scale
            # 原图像对应点与比例矩阵对应点相乘
            img[i][j] = round(img[i][j] * shading[i][j])
    # 将RAW图像转换为CFA差值后的图像
    dst = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2BGR)

    # cv2.imshow('shading', dst)
    # cv2.waitKey(0)
    return dst


# '''
#下面几行代码用来验证增强结果
src = cv2.imread("../VOCdevkit/VOC2007/JPEGImages/000000.jpg")
# src = cv2.imread("img.png")
rain_drop = lens_shading_error(src, 0.1)
cv2.imshow('augmentation img', rain_drop)
cv2.waitKey(0)
# '''
