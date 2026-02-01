import cv2

#Reading the Image
originalImage = cv2.imread('Images\Planet 1.jpg')
resizeImage = cv2.resize(originalImage, (1000, 800))

#Displaying the Image
cv2.imshow('Planet 1', resizeImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
