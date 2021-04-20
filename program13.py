import cv2
import numpy as np

img = cv2.imread('color_balls.png')
gray = cv2.imread('color_balls.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow("Image2",gray)

ret, img2 = cv2.threshold(gray, 254, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Image3",img2)

label = cv2.connectedComponentsWithStats(img2)

n = label[0] - 1
data = np.delete(label[2], 0, 0)
center = np.delete(label[3], 0, 0)

for i in range(n):
    x1 = data[i][0]
    y1 = data[i][1]
    x2 = x1 + data[i][2]
    y2 = y1 + data[i][3]
    cv2.rectangle(img, (x1,y1), (x2,y2), (0,0,0))

cv2.imshow("Image",img)

key = cv2.waitKey(0)

cv2.destroyWindow("Image1")
cv2.destroyWindow("Image2")
cv2.destroyWindow("Image3")

