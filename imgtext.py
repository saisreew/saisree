import cv2
import numpy as np
img = cv2.imread('text.jpg')
retval, threshold = cv2.threshold(img, 80, 225, cv2.THRESH_BINARY)
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 130, 225, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayscaled, 225, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('gaus',gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()