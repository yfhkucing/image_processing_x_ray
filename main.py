import cv2
import numpy as np
import contrast 
import clache

Path = "images\WhatsApp Image 2022-12-06 at 11.07.36 (2).jpeg"


def image_filter(path):
    kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
    kernel2 = np.array([[-1, -1, -1],
                   [-1, 9,-1],
                   [-1, -1, -1]])
    while True :
        img = cv2.imread(path)
        img = contrast.contrast_new(img,1.5)
        img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
        img = cv2.filter2D(src=img, ddepth=-10, kernel=kernel)
        img = cv2.bitwise_not(img)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #img = img = cv2.fastNlMeansDenoising(img)
        img = cv2.pyrUp(img)
        #img = cv2.filter2D(img, -1 ,kernel2)
        cv2.imshow('results',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
if __name__ == "__main__":
    image_filter(Path)