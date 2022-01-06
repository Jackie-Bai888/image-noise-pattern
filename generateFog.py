import cv2
import math

def fog(img, pot=0.1):
    """
     #生成雾场景图像
     输入:
         img     图像
         A  根据大气散射模型控制亮度
         pot 控制雾的浓度
     返回雾场景图像
     """
    # cv2.imshow("src", img)
    # beta = 1  # 雾的浓度
    bright = 0.75+0.1-pot #亮度,浓度越大亮度越小，浓度最大值0.1，亮度最小值0.5，因此在最小值上叠加
    img_f = img / 255.0
    (row, col, chs) = img.shape
    # 雾化尺寸
    size = math.sqrt(max(row, col))
    # 雾化中心为图像中上部分，该部分视野距离最远
    center = (row//5, col//2)
    # center = (row*row_pro, col*col_pro)
    # 根据大气散射模型依据距雾化中心的距离，对对应像素点进行处理
    for j in range(row):
        for k in range(col):
            d = -0.04 * math.sqrt((j - center[0]) ** 2 + (k - center[1]) ** 2) + size
            td = math.exp(-pot * d)
            img_f[j][k][:] = img_f[j][k][:] * td + bright * (1 - td)
            # img_f[j][k][:] = img_f[j][k][:]*255   #使得整个图片都变白了
    return img_f


# '''
#下面几行代码用来验证增强结果
src = cv2.imread("../VOCdevkit/VOC2007/JPEGImages/000000.jpg")
cv2.imshow('original img', src)
black_src = fog(src)
cv2.imshow('color img', black_src)
cv2.waitKey(0)
# '''


