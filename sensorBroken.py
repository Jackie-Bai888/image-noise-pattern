import cv2
import numpy as np
import random


def sensor_broken(img, spot = True, deviation = True, leak = True):
    """
     #激光照射导致感光芯片异常
     输入:
         img     图像
         spot      是否产生光斑
         deviation  是否产生色彩偏差
         leak    是否因激光照射产生感光单元失效融化
     返回摄像头芯片时序异常后的图像
     """
    des = img
    # 随机生成激光照射点的X,Y坐标
    x = int(random.uniform(0, img.shape[0]))
    y = int(random.uniform(100, img.shape[1]) - 100)


    if spot:
        # 如果产生光斑，则随机在图像上选择是个中心
        img_spot = np.zeros(img.shape, np.uint8)
        i = 10
        while i > 0:
            center = (int(random.uniform(0, img.shape[1])), int(random.uniform(0, img.shape[0])))
            # 对每个中心随机选择半径进行光斑填充
            cv2.circle(img_spot, center, int(random.uniform(1, 7)), (0, 0, 255), -1)
            i -= 1
        des = cv2.addWeighted(img, 1, img_spot, random.uniform(0.4, 0.7), 0)
    if deviation:
        # 如果产生色彩偏移，则在激光照色点附近生成竖条状，渐变色彩偏差
        img_deviation = np.zeros(img.shape, np.uint8)
        # 竖条状色彩偏移宽度
        i = 50
        # 色彩偏移的中轴线位置
        axis = int(random.uniform(10, 20))
        while i >= 0:
            img_deviation[:, y - i + axis, 0] = 255 - i * 5 - 5
            img_deviation[:, y - i + axis, 2] = 255 - i * 5 - 5
            i -= 1
        j = 50
        while j > 0:
            img_deviation[:, y + j + axis, 0] = 255 - j * 5 - 5
            img_deviation[:, y + j + axis, 2] = 255 - j * 5 - 5
            j -= 1
        # 对该条状位置进行图像融合
        des = cv2.addWeighted(des, 1, img_deviation, 0.6, 0)
    if leak:
        # 如果发生感光元件融化，则随机生成类似抛物线形状融化区域，并将该区域置为黑色
        axis = int(random.uniform(10, 30))
        des[x - 1:x + 1, :, :] = 0
        i = 0
        while i < 40:
            des[x:int(x + 16 - (i / 10) ** 2) + int(random.uniform(0, 20 - i // 2)), y - i + axis, :] = 0
            i += 1
        j = 0
        while j < 40:
            des[x:int(x + 16 - (j / 10) ** 2) + int(random.uniform(0, 20 - j // 2)), y + j + axis, :] = 0
            j += 1
    else:
        print('----')
        # 随机生成因感光单元失效后十字线的颜色
        r = int(random.uniform(0, 255))
        g = int(random.uniform(0, 255))
        b = int(random.uniform(0, 255))
        # 给十字线填充颜色
        des[:, y:y + 1, 0] = b
        des[:, y:y + 1, 1] = g
        des[:, y:y + 1, 2] = r
    return des


# '''
#下面几行代码用来验证增强结果
src = cv2.imread("../VOCdevkit/VOC2007/JPEGImages/000000.jpg")
augument_image = sensor_broken(src)
cv2.imshow('augument image', augument_image)
cv2.waitKey(0)
# '''
