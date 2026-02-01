import cv2

mountains = cv2.imread('Classwork\Images\Mountains.jpg')

cv2.imshow('Mountains', mountains)
cv2.waitKey(0)

#Rotating a Image
(height, width) = mountains.shape[:2]
print(height, width)

centre = width//2, height//2

newMatrix = cv2.getRotationMatrix2D(centre, 90, 1)
rotateImage = cv2.warpAffine(mountains, newMatrix, (width, height))

cv2.imshow('Roatated Image', rotateImage)
cv2.waitKey(0)

#Resizing Image
resizedImage = cv2.resize(mountains, (100, 100))
cv2.imshow('Resize Image', resizedImage)
cv2.waitKey(0)

cv2.destroyAllWindows()
