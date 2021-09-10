import cv2
import glob
import os

img0 = cv2.imread('im0.jpg', 1)

img1 = cv2.imread('im1.jpg', 1)

img2 = cv2.imread('im2.jpg', 1)

b0, g0, r0 = cv2.split(img0)
b1, g1, r1 = cv2.split(img1)
b2, g2, r2 = cv2.split(img2)

image = cv2.merge((b0, g1, r2))

cv2.imshow('image', image)
cv2.imwrite('merge_result.jpg', image) 
cv2.waitKey(0)

cv2.destroyAllWindows()