import cv2

img = cv2.imread('mandrill.jpg')
mask = cv2.imread('mask.png')

img2 = img * (mask / 255.0) 

cv2.imshow("Image",img)
cv2.imshow("Mask",mask)
cv2.imshow("Image2",img2.astype("uint8"))

key = cv2.waitKey(0)

cv2.destroyWindow("Image")
cv2.destroyWindow("Mask")
cv2.destroyWindow("Image2")
