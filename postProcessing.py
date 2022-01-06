import numpy as np
import cv2
import random

def blur(img):
    """
    #生成失焦图像
    输入:
        img 图像
    返回：
        模糊后的图像
    """
    # 高斯模糊核大小为3*3
    gauss_blur = cv2.GaussianBlur(img, (3, 3), 0, 0)
    return gauss_blur


def sp_noise(img, precent=0.01):
    '''
    添加椒盐噪声
    prob:噪声比例
    '''
    image = blur(img)
    output = np.zeros(img.shape, np.uint8)
    thres = 1 - precent
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.randint(1,10)/10
            if rdn < precent:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


def gasuss_noise(img, mean=0, var=0.001):
    '''
        添加高斯噪声
        mean : 均值
        var : 方差
    '''
    image = blur(img)
    image = np.array(image / 255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out * 255)
    # cv.imshow("gasuss", out)
    return out

# '''
#下面几行代码用来验证增强结果
src = cv2.imread("../VOCdevkit/VOC2007/JPEGImages/000000.jpg")
blur_image = blur(src)
sp_image = sp_noise(src, 0.2)
ga_image = gasuss_noise(src)
# cv2.imshow('blur image', blur_image)
# cv2.imshow('sp image', sp_image)
cv2.imshow('ga image', ga_image)
cv2.waitKey(0)
# '''
