import cv2 as cv
import numpy as np
import argparse
# Read image given by user

def contrast_grayscale(image,alpha,beta):
    #image = cv.imread("images\WhatsApp Image 2022-12-06 at 11.07.36 (2).jpeg")
    new_image = np.zeros(image.shape, image.dtype)
    alpha = alpha # Simple contrast control
    beta = beta    # Simple brightness control

    # Do the operation new_image(i,j) = alpha*image(i,j) + beta
    # Instead of these 'for' loops we could have used simply:
    # new_image = cv.convertScaleAbs(image, alpha=alpha, beta=beta)
    # but we wanted to show you how to access the pixels :)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            new_image[y,x] = np.clip(alpha*image[y,x] + beta, 0, 255)
    
    return new_image

def contrast_color(image,alpha,beta):
    #image = cv.imread("images\WhatsApp Image 2022-12-06 at 11.07.36 (2).jpeg")
    new_image = np.zeros(image.shape, image.dtype)
    alpha = alpha # Simple contrast control
    beta = beta    # Simple brightness control

    # Do the operation new_image(i,j) = alpha*image(i,j) + beta
    # Instead of these 'for' loops we could have used simply:
    # new_image = cv.convertScaleAbs(image, alpha=alpha, beta=beta)
    # but we wanted to show you how to access the pixels :)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)
    
    return new_image

def contrast_new(img,clipLimit):
    # converting to LAB color space
    lab= cv.cvtColor(img, cv.COLOR_BGR2LAB)
    l_channel, a, b = cv.split(lab)

    # Applying CLAHE to L-channel
    # feel free to try different values for the limit and grid size:
    clahe = cv.createCLAHE(clipLimit=clipLimit, tileGridSize=(8,8))
    cl = clahe.apply(l_channel)

    # merge the CLAHE enhanced L-channel with the a and b channel
    limg = cv.merge((cl,a,b))

    # Converting image from LAB Color model to BGR color spcae
    enhanced_img = cv.cvtColor(limg, cv.COLOR_LAB2BGR)

    # Stacking the original image with the enhanced image
    return enhanced_img

