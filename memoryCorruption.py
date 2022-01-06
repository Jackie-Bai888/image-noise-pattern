import numpy as np
import cv2
import random
import least_object


def memory_corruption(img):
    """
     缓存随机损坏异常
     输入:
         image     图像
     返回缓存随机损坏异常后的图像
     """
    # 分离RGB通道
    b, g, r = cv2.split(img)
    row, col, chs = img.shape
    # 随机生成矩阵0 表示内存损坏
    damageB = np.random.randint(0, 256, img.shape[0:2], dtype=np.uint8)
    damageG = np.random.randint(0, 256, img.shape[0:2], dtype=np.uint8)
    damageR = np.random.randint(0, 256, img.shape[0:2], dtype=np.uint8)

    # 阈值处理 大于1的置为1
    tB, damageB = cv2.threshold(damageB, 32, 255, cv2.THRESH_BINARY)
    tG, damageG = cv2.threshold(damageG, 32, 255, cv2.THRESH_BINARY)
    tR, damageR = cv2.threshold(damageR, 32, 255, cv2.THRESH_BINARY)
    # 图像按位与运算 损坏的点置为0
    b = cv2.bitwise_and(b, damageB)
    g = cv2.bitwise_and(g, damageG)
    r = cv2.bitwise_and(r, damageR)

    # 将RGB通道进行融合
    dst = cv2.merge([b, g, r])
    # cv2.imshow('dst', dst)
    # cv2.waitKey(0)
    return dst


# 按块损坏
def memory_damage(img, img_name, num_precent=1):
    """
         #缓存按块损坏异常
         输入:
             image     图像
         返回缓存按块损坏异常后的图像
    """
    B, G, R = cv2.split(img)
    row, col, chs = img.shape
    least_object_height, least_object_width = least_object.get_least_object_height_width(img_name)
    damage_row, damage_col = int((least_object_height//2)*num_precent), int((least_object_width//2)*num_precent)
    start_row = random.randint(0, row-damage_row-1)
    start_col = random.randint(0, col-damage_col-1)
    img[start_row:start_row+damage_row, start_col:start_col+damage_col] = [0,0,0]
    return img

# '''
#下面几行代码用来验证增强结果
src = cv2.imread("../VOCdevkit/VOC2007/JPEGImages/000000.jpg")
md = memory_damage(src, '000000.jpg', 1)
cv2.imshow('md image', md)
cv2.waitKey(0)
# '''
