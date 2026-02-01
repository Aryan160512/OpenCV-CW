import cv2

openCV = cv2.imread('Images\OpenCV Logo.png')

saturatedImageB, saturatedImageG, saturatedImageR = cv2.split(openCV)

cv2.imshow('OpenCV Original Image', openCV)
cv2.waitKey(0)

cv2.imshow('OpenCV Blue Saturation', saturatedImageB)
cv2.waitKey(0)

cv2.imshow('OpenCV Green Saturation', saturatedImageG)
cv2.waitKey(0)

cv2.imshow('OpenCV Red Saturation', saturatedImageR)
cv2.waitKey(0)

cv2.destroyAllWindows()
