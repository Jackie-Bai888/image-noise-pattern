import numpy as np
import cv2


def RGB2Bayer_RG(img):
    """
     #CFA插值异常
     输入:
         img     图像
     返回CFA异常后的图像
     """
    # 获取图像长宽通道数
    row, col, chl = img.shape
    # 长度宽度做成4的倍数，因为一般sensor为了符合最小的拜耳单元，长宽都是4的倍数
    ext_x, ext_y = row % 4, col % 4
    # 将重新定义的宽高图像赋值给img
    img = img[0:row - ext_x, 0:col - ext_y, :]
    # 重新获取图像属性
    row, col, chl = img.shape

    # 假设图片为拜耳格式RG，根据像素的位置，把其他2个通道都赋0，然后得到一张假的raw
    img[0:row:2, 0:col:2, 0:2] = 0, 0  #R
    img[0:row:2, 1:col:2, [0, 2]] = 0, 0  #G
    img[1:row:2, 0:col:2, [0, 2]] = 0, 0  #G
    img[1:row:2, 1:col:2, 1:3] = 0, 0  #B



    # 此时仍为三通道图像
    # cv2.imshow('cvt_RG.jpg', img)

    # 生成RAW单通道图像
    raw = np.zeros((row, col), dtype=np.uint8)
    raw[0:row:2, 0:col:2] = img[0:row:2, 0:col:2, 2]  # red
    raw[0:row:2, 1:col:2] = img[0:row:2, 1:col:2, 1]  # green
    raw[1:row:2, 0:col:2] = img[1:row:2, 0:col:2, 1]  # green
    raw[1:row:2, 1:col:2] = img[1:row:2, 1:col:2, 0]  # blue
    # raw.tofile('cvt_RG.raw')  # 8bit
    #此时为单通道图像
    return raw


'''
#下面几行代码用来验证增强结果
src = cv2.imread("../VOCdevkit/VOC2007/JPEGImages/000000.jpg")
raw_image = RGB2Bayer_RG(src)
cv2.imshow('raw image', raw_image)
cv2.waitKey(0)
'''
