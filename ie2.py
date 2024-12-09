import numpy as np
import cv2

def on_change(value):
    pass

img = cv2.imread('girl.jpeg',1)
new_image = np.zeros(img.shape, img.dtype)


cv2.namedWindow('image',cv2.WINDOW_GUI_NORMAL)
cv2.createTrackbar('slider', 'image' , 0, 6,lambda x:x)
bright = cv2.getTrackbarPos('slider','image')
contrast=1


for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        for c in range(img.shape[2]):
            new_image[y,x,c] = np.clip(contrast*img[y,x,c] + bright, 0, 255)


cv2.imshow('image', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()