import cv2

img = cv2.imread('mandrill.jpg')
mask = cv2.imread('mask.png')

cv2.imshow("Image",img)
cv2.imshow("Mask",mask)

img2 = img * (mask / 255.0) 

cv2.imshow("Image2",img2.astype("uint8"))

key = cv2.waitKey(0)

cv2.destroyWindow("Image")
