import cv2
import math

def fog(img, pot=0.1):
    # cv2.imshow("src", img)
    # beta = 1  
    bright = 0.75+0.1-pot 
    img_f = img / 255.0
    (row, col, chs) = img.shape
    size = math.sqrt(max(row, col))
    center = (row//5, col//2)
    # center = (row*row_pro, col*col_pro)
    
    for j in range(row):
        for k in range(col):
            d = -0.04 * math.sqrt((j - center[0]) ** 2 + (k - center[1]) ** 2) + size
            td = math.exp(-pot * d)
            img_f[j][k][:] = img_f[j][k][:] * td + bright * (1 - td)
            # img_f[j][k][:] = img_f[j][k][:]*255   
    return img_f


# '''
#test
src = cv2.imread("../VOCdevkit/VOC2007/JPEGImages/000000.jpg")
cv2.imshow('original img', src)
black_src = fog(src)
cv2.imshow('color img', black_src)
cv2.waitKey(0)
# '''


