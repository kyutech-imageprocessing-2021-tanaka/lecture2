import cv2
import numpy as np

img = cv2.imread('color_balls.png')
gray = cv2.imread('color_balls.png', cv2.IMREAD_GRAYSCALE)

ret, img2 = cv2.threshold(gray, 254, 255, cv2.THRESH_BINARY_INV)

label = cv2.connectedComponentsWithStats(img2)

n = label[0]
bbox = label[2]
center = label[3]

for i in range(1,n):
    x1 = bbox[i][0]
    y1 = bbox[i][1]
    x2 = x1 + bbox[i][2]
    y2 = y1 + bbox[i][3]
    cv2.rectangle(img, (x1,y1), (x2,y2), (0,0,0))
    cx = int( center[i][0] )
    cy = int( center[i][1] )
    cv2.circle(img, (cx,cy), 5, (0,0,0), -1)

cv2.imshow("Image",img)
cv2.imshow("Image2",gray)
cv2.imshow("Image3",img2)

key = cv2.waitKey(0)

cv2.destroyWindow("Image1")
cv2.destroyWindow("Image2")
cv2.destroyWindow("Image3")

