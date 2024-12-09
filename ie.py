import numpy as np
import cv2

 # Loading pictures Read color images normalized and converted to floating-point
image = cv2.imread('girl.jpeg', cv2.IMREAD_COLOR).astype(np.float32) / 255.0

 # Color space conversion BGR to HLS
hlsImg = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

 # Slide the maximum value
MAX_VALUE = 10
MAX_VALUE2 = 100
 #     minimum
MIN_VALUE = 0

 # Regulate the window of saturation and brightness
cv2.namedWindow("image enhancement")

 # Create a slider
cv2.createTrackbar("brigthness", "image enhancement", MIN_VALUE, MAX_VALUE, lambda x:x)
cv2.createTrackbar("saturation", "image enhancement", MIN_VALUE, MAX_VALUE2, lambda x:x)

 
while True:
         #      
    hlsCopy = np.copy(hlsImg)
         # Get the values ​​of Lightness and Saturation
    lightness = cv2.getTrackbarPos("brigthness", "image enhancement")
    saturation = cv2.getTrackbarPos('saturation', "image enhancement")
         # Adjust the brightness
    hlsCopy[:, :, 1] = (1.0 + lightness / float(MAX_VALUE)) * hlsCopy[:, :, 1]
    hlsCopy[:, :, 1][hlsCopy[:, :, 1] > 1] = 1
         # saturation 
    hlsCopy[:, :, 2] = (1.0 + saturation / float(MAX_VALUE2)) * hlsCopy[:, :, 2]
    hlsCopy[:, :, 2][hlsCopy[:, :, 2] > 1] = 1
    # HLS2BGR
    lsImg = cv2.cvtColor(hlsCopy, cv2.COLOR_HLS2BGR)
         # Display the adjusted effect
    cv2.imshow("image enhancement", lsImg)
    ch = cv2.waitKey(5)
         # Press the ESC button to exit
    if ch == 27:
        break
    elif ch == ord('s'):
                 # Press the S button to save and exit
        lsImg = lsImg * 255
        lsImg = lsImg.astype(np.uint8)
        cv2.imwrite("./output/lsImg.jpg", lsImg)
        break
    
Print ("Lightness):", INT (Lightness))
Print ("Saturation):", int (SaTURATION))
  # Close all windows
cv2.destroyAllWindows()