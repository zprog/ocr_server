import cv2
import numpy as np
#from . import ocr_core
from PIL import Image
import pytesseract
#b64 decode strip mime
import base64

def ocr_init():
    #ORIGINAL_IMAGE = "IMG_4031.jpg"
    ORIGINAL_IMAGE = ""
    #image = cv2.imread("images/" + ORIGINAL_IMAGE)

def ocr(ORIGINAL_IMAGE):
    # image = cv2.imread("static/uploads/" + ORIGINAL_IMAGE)
    nparr = np.frombuffer(np.frombuffer(base64.decodebytes(ORIGINAL_IMAGE), dtype="np.float64"))
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    roi = image
    #convert to grey
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    #threshold image
    thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]
    print("TRESH: " + pytesseract.image_to_string(thresh))

    # apply morphology to clean up small white or black regions
    kernel = np.ones((5,5), np.uint8)
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    morph = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel)

    # thin region to remove excess black border
    kernel = np.ones((3,3), np.uint8)
    morph = cv2.morphologyEx(morph, cv2.MORPH_ERODE, kernel)

    print("MORPH: " + pytesseract.image_to_string(morph))

    img = roi

    # applying different thresholding
    # techniques on the input image
    # all pixels value above 120 will
    # be set to 255
    ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

    # the window showing output images
    # with the corresponding thresholding
    # techniques applied to the input images
#    cv2.imshow('Binary Threshold', thresh1)
#    cv2.imshow('Binary Threshold Inverted', thresh2)
#    cv2.imshow('Truncated Threshold', thresh3)
#    cv2.imshow('Set to 0', thresh4)
#    cv2.imshow('Set to 0 Inverted', thresh5)

    print("t1: " + pytesseract.image_to_string(thresh1))
    print("t2: " + pytesseract.image_to_string(thresh2))
    print("t3: " + pytesseract.image_to_string(thresh3))
    print("t4: " + pytesseract.image_to_string(thresh4))
    print("t5: " + pytesseract.image_to_string(thresh5))
    thresh_dict = {
            'Origin': pytesseract.image_to_string(roi),
            'M0': pytesseract.image_to_string(morph),
            'T0': pytesseract.image_to_string(thresh),
            'T1': pytesseract.image_to_string(thresh1),
            'T2': pytesseract.image_to_string(thresh2),
            'T3': pytesseract.image_to_string(thresh3),
            'T4': pytesseract.image_to_string(thresh4),
            'T5': pytesseract.image_to_string(thresh5)
            }

    print(pytesseract.image_to_string(roi))
    return thresh_dict

