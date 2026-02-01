import cv2

originalImage = cv2.imread('Images\Pikachu.png')

cv2.imshow('Pikachu', originalImage)
cv2.waitKey(0)

greyscaledImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
cv2.imshow('Greyscaled Pikachu', greyscaledImage)

#Loading a Image in Greyscaled format

peopleWalking = cv2.imread('Images\People Walking.jpeg', 1)
cv2.imshow('Greyscaled People Walking', peopleWalking)
cv2.waitKey(0)

#Saving the Greyscaled Image

cv2.imwrite('Introduction to OpenCV/greyscaledPikachu.png', greyscaledImage)
print('Successfully Saved Image')
cv2.waitKey(0)

#Coverting a image into HSV

hsvImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Pikachu', hsvImage)
cv2.waitKey(0)

mountains = cv2.imread('Images\Mountains.jpg')
cv2.imshow('Mountains', mountains)
cv2.waitKey(0)

mountainsHSV = cv2.cvtColor(mountains, cv2.COLOR_BGR2HSV)
cv2.imshow('Mountains HSV', mountainsHSV)
cv2.waitKey(0)

cv2.destroyAllWindows()