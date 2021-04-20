import cv2

img = cv2.imread('color_balls.png', cv2.IMREAD_GRAYSCALE)

canny_img = cv2.Canny(img, 50, 110)

cv2.imshow("Image",img)
cv2.imshow("Image2",canny_img)

key = cv2.waitKey(0)

cv2.destroyWindow("Image")
cv2.destroyWindow("Image2")
