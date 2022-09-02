from skimage import exposure
import cv2
def gamma_correction(img, gamma_par=2):
    gamma_corrected = exposure.adjust_gamma(img, gamma_par)
    return gamma_corrected

# '''
#test
src = cv2.imread("../VOCdevkit/VOC2007/JPEGImages/000000.jpg")
cv2.imshow('original img', src)
gamma_img = gamma_correction(src, 4)
cv2.imshow('gamma img', gamma_img)
cv2.waitKey(0)
# '''
