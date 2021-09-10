import cv2
import glob
import os

img = cv2.imread('result.jpg',1)

b, g, r = cv2.split(img)
cv2.imshow('image0', b)
cv2.imwrite('blue.jpg', b) 
cv2.waitKey(0)
cv2.imshow('image1', g)
cv2.imwrite('green.jpg', g) 
cv2.waitKey(0)
cv2.imshow('image2', r)
cv2.imwrite('red.jpg', r) 
cv2.waitKey(0)
image = cv2.merge((b, g, r))
cv2.imshow('image', image)
cv2.waitKey(0)

cv2.destroyAllWindows()