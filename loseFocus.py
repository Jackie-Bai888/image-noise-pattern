import cv2
import random

def lose_focus(img, level=10):
    """
    #生成失焦图像,这里使用高斯模糊来模拟
    输入:
        img 图像
        mold 模糊类型
        level 模糊等级
    返回：
        模糊后的图像
    """
    mold = 1#random.randint(0,1)
    if mold == 0:
        # 均值模糊
        mean_blur = cv2.blur(img, (level * 2 - 1, level * 2 - 1))
        return mean_blur
    else:
        # 高斯模糊
        gauss_blur = cv2.GaussianBlur(img, (level * 2 - 1, level * 2 - 1), 0, 0)
        return gauss_blur


# '''
#下面几行代码用来验证增强结果
src = cv2.imread("../VOCdevkit/VOC2007/JPEGImages/000000.jpg")
# cv2.imshow('original img', src)
error_img = lose_focus(src)
cv2.imshow('augmentation img', error_img)
cv2.waitKey(0)
# '''
