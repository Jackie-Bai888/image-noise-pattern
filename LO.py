import cv2
import numpy as np
import random


def generate_rain_drop(img, count=100):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    img[:, :, 0] = img[:, :, 0] * 0.7
    img = cv2.cvtColor(img, cv2.COLOR_YUV2BGR)
    # 雨滴计数器
    i = 0
    # cv2.imshow('res', img)
    while i < count:
        # 雨点坐标
        y = int(random.uniform(0, img.shape[0]))
        x = int(random.uniform(0, img.shape[1]))
        height = int(200 + random.uniform(0, 170))
        weight = int(height * random.uniform(0.6, 0.8))
        roi = img[min(max(0, y - height // 2), img.shape[0] - height):min(max(0, y - height // 2),
                                                                          img.shape[0] - height) + height,
              min((max(0, x - weight // 2)), img.shape[1] - weight):min((max(0, x - weight // 2)),
                                                                        img.shape[1] - weight) + weight]
        scale = 0.08-count/10000#random.uniform(0.04, 0.07)
        rain_height = int(height * scale)
        rain_weight = int(weight * scale)
        temp = np.zeros((rain_height, rain_weight, 3), np.uint8)
        mask = np.zeros([rain_height, rain_weight], np.uint8)
        rain = cv2.resize(roi, (rain_weight, rain_height))
        cv2.ellipse(mask, (rain_weight // 2, rain_height // 2), (rain_weight // 2, rain_height // 2), 0, -180, 180, 255,
                    -1)
        cv2.copyTo(rain, mask, temp)
        cv2.flip(temp, 0, temp)
        cv2.flip(temp, 1, temp)
        for j in range(rain_height):
            for k in range(rain_weight):
                if temp[j, k, 0] != 0 and temp[j, k, 1] != 0 and [j, k, 2] != 0:
                    if 0 <= y - rain_height // 2 + j < img.shape[0] and 0 <= x - rain_weight // 2 + k < img.shape[1]:
                        img[y - rain_height // 2 + j, x - rain_weight // 2 + k, 0] = temp[j, k, 0]
                        img[y - rain_height // 2 + j, x - rain_weight // 2 + k, 1] = temp[j, k, 1]
                        img[y - rain_height // 2 + j, x - rain_weight // 2 + k, 2] = temp[j, k, 2]
                else:
                    continue
        i += 1
    return img


# '''
src = cv2.imread("../VOCdevkit/VOC2007/JPEGImages/000000.jpg")
cv2.imshow('original img', src)
rain_drop = generate_rain_drop(src,500)
cv2.imshow('augmentation img', rain_drop)
cv2.waitKey(0)
# '''
