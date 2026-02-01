import cv2

people = cv2.imread('Classwork\Images\People Walking.jpeg')
line = cv2.line(people, (350, 300), (350, 500), (255, 0, 0), 10, 1)
cv2.rectangle(people, (300, 10), (400, 300), (0, 0, 0), -1, 1)
cv2.circle(people, (350, 50), 30, (0, 0, 255), -1)
cv2.circle(people, (350, 150), 30, (0, 255, 255), -1)
cv2.circle(people, (350, 250), 30, (0, 255, 0), -1)

cv2.putText(people, 'Stop', (330, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1, 1)
cv2.putText(people, 'Ready', (330, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1, 1)
cv2.putText(people, 'Go', (330, 250), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1, 1)

cv2.imshow('People Walking', people)
cv2.waitKey(0)

cv2.destroyAllWindows()