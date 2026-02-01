import cv2

planet3 = cv2.imread('Classwork\Images\Planet 3.jpg')
planet2 = cv2.imread('Classwork\Images\Planet 2.jpg')


#Image Addition

planetsAdded = cv2.addWeighted(planet3, 0.5, planet2, 0.5, 0)

cv2.imshow('Planets Addition', planetsAdded)
cv2.waitKey(0)

# Image Subtraction
planetsSubtracted1 = cv2.subtract(planet3, planet2)

cv2.imshow('Planets Subtraction', planetsSubtracted1)
cv2.waitKey(0)

planetsSubtracted2 = cv2.subtract(planet2, planet3)

cv2.imshow('Planet Subtraction 2', planetsSubtracted2)
cv2.waitKey(0)

cv2.destroyAllWindows()

