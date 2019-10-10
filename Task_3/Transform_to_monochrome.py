# python 3.6
import cv2


img = cv2.imread('shrek.jpg')
cv2.imshow('Image before transformation', img)
cv2.waitKey()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 199, 5)

thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY, 199, 5)
cv2.imshow('Adaptive Mean', thresh1)
cv2.waitKey()
cv2.imshow('Adaptive Gaussian', thresh2)
cv2.waitKey()
