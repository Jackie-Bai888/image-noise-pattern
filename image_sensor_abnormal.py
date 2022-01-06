'''
该模块主要是用来模拟图像传感器异常而导致成像有噪音。
造成损伤的原因：激光照射；
损伤分类(按照从严重等级)：点损伤、线损伤、面损伤;
note：因面损伤会导致图像全白，导致根本无法无法进行目标检测，所以不模拟
'''
from RGB2RAW import RGB2Bayer_RG
import cv2
import random
import numpy as np

def sensor_damage(img, h, w, num = 25, sensor='ccd'):
    '''
    该函数用来模拟点损伤中图片出现的光斑
    num :损伤点的个数
    max_l:椭圆长轴的最大值
    damage_grade:损伤值。当<3时是点损伤，否则就是线损伤。线损伤时，damage值越大则线越宽
    '''
    max_l = 4
    damage_grade = 3
    axes_l = random.randint(max_l//2+1, max_l)
    axes_s = axes_l//2
    axesSize = (axes_l, axes_s)  # 随机生成椭圆的长轴和短轴
    ptCenter = (random.randint(axesSize[1] // 2, w - axesSize[1] // 2),
                random.randint(axesSize[0] // 2, h - axesSize[0] // 2))  # 中心点位置
    while num > 0:
        rotateAngle = 90  # 旋转角度为 90
        startAngle = 0
        endAngle = 360
        point_color = (255, 255, 255)  # BGR
        thickness = -1
        lineType = 4
        cv2.ellipse(img, ptCenter, axesSize, rotateAngle, startAngle, endAngle, point_color, thickness, lineType)
        if damage_grade > 2:
            if sensor == 'ccd':
                cv2.line(img, (ptCenter[0], 0), (ptCenter[0], h), (255, 255, 255), damage_grade-2, 8)
            else:
                cv2.line(img, (0, ptCenter[1]), (w, ptCenter[1]), (0, 0, 0), damage_grade - 2, 8)
                cv2.line(img, (ptCenter[0], 0), (ptCenter[0], h), (0, 0, 0), damage_grade - 2, 8)

        num -= 1
        new_axes_l = random.randint(max_l//2+1, max_l)
        new_axes_s = new_axes_l//2
        axesSize = (new_axes_l, new_axes_s)  # 随机生成椭圆的长轴和短轴
        while True:
            '''新的椭圆中心不能在旧椭圆的位置范围内'''
            new_x = random.randint(axesSize[1] // 2, w - axesSize[1] // 2)
            new_y = random.randint(axesSize[0] // 2, h - axesSize[0] // 2)
            if new_x-new_axes_l//2 > ptCenter[0]+axes_l//2 or new_x+new_axes_l//2 < ptCenter[0]-axes_l//2 or \
                    new_y-new_axes_s//2 > ptCenter[1]+axes_s//2 or new_y+new_axes_s//2 < ptCenter[1]-axes_s//2:
                break
        ptCenter = (new_x, new_y)  # 中心点位置

    # new_img = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2BGR)
    return img


if __name__ == '__main__':
    path = '../VOCdevkit/VOC2007/JPEGImages/000000.jpg'
    img = cv2.imread(path)
    cv2.imshow('ori', img)
    h, w, _ = img.shape
    # img = RGB2Bayer_RG(img) #将图像变为raw格式
    # new_img = sensor_damage(img, h, w, 50,'ccd')
    # cv2.imshow('test1', new_img)
    new_img = sensor_damage(img, h, w, 50, 'cmos')
    cv2.imshow('test2', new_img)
    cv2.waitKey(0)