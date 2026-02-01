import cv2

pikachu = cv2.imread('Classwork\Images\Pikachu.png')

edges = cv2.Canny(pikachu, 100, 200)

cv2.imshow('Edges', edges)
cv2.waitKey(0)

cv2.destroyAllWindows()