import numpy as np
import cv2
import random
import least_object


def timing_error(img, img_name):
    """
     #摄像头芯片时序异常
     输入:
         img     图像
     返回摄像头芯片时序异常后的图像
     """
    # 生成一张黑色图像，留黑部分为由于时序错乱未填充部分。图像大小和类型与输入图像一致
    des = np.zeros(img.shape, np.uint8)
    # 获取图像的宽高和通道数
    row, col, chs = img.shape
    # 随机生成时序异常发生的次数
    least_object_height,_ = least_object.get_least_object_height_width(img_name)
    print(least_object_height)
    errorNum = int(random.randint(0, least_object_height//2))
    # 记录异常发生处所在行数
    error = []
    # 异常发生计数器
    gapCount = 0
    # 随机生成异常行
    for i in range(errorNum):
        error.append(int(random.uniform(0, row)))
    error.sort()

    # 根据异常行数和异常发生次数对异常图像进行填充生成
    des[0:error[0], 0:col, 0:chs] = img[0:error[0], 0:col, 0:chs]
    for i in range(errorNum-1):
        # 每次异常持续时间（行数）
        gap = int(random.uniform(10, 20))
        gapCount = gapCount + gap
        # 超过原图行数退出循环
        if error[i]+gapCount > row or error[i+1]+gapCount > row:
            des[error[i]:row-gapCount, 0:col, 0:chs] = img[error[i]+gapCount:row, 0:col, 0:chs]
            break
        # 将原图像中对应位置行填充到异常图像位置行
        else:
            des[error[i]:error[i + 1], 0:col, 0:chs] = img[error[i] + gapCount:error[i + 1] + gapCount, 0:col, 0:chs]
    # 对剩余行进行填充
    des[error[errorNum-1]:row-gapCount, 0:col, 0:chs] = img[error[errorNum-1] + gapCount:row, 0:col, 0:chs]
    # cv2.imshow('des', des)
    # cv2.imshow('res', image)
    # cv2.waitKey(0)
    return des

def sensor_timing_error(img, img_name, row_precent=1):
    row, col, chs = img.shape
    least_object_height = least_object.get_least_object_height(img_name)
    errorNum = int((least_object_height//2)*row_precent)
    error_start = random.randint(0, row-errorNum-1)
    img[error_start:error_start+errorNum, :] = (0, 0, 0)
    return img

# '''
#下面几行代码用来验证增强结果
src = cv2.imread("../VOCdevkit/VOC2007/JPEGImages/000000.jpg")
augument_image = sensor_timing_error(src, '000000.jpg')
cv2.imshow('augument image', augument_image)
cv2.waitKey(0)
# '''