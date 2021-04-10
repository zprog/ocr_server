import cv2
import numpy as np
from PIL import Image
import pytesseract
import base64

def ocr(ORIGINAL_IMAGE):
    nparr = np.frombuffer(base64.decodebytes(ORIGINAL_IMAGE), dtype="uint8")
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    roi = image
    #convert to grey
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    #threshold image
    thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

    # apply morphology to clean up small white or black regions
    kernel = np.ones((5,5), np.uint8)
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    morph = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel)

    # thin region to remove excess black border
    kernel = np.ones((3,3), np.uint8)
    morph = cv2.morphologyEx(morph, cv2.MORPH_ERODE, kernel)

    img = roi

    # applying different thresholding techniques on the input image
    # all pixels value above 120 will be set to 255
    ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

    # the first two: morph and thresh seem to be the best over all.
    # let's use those too and see how it affects performance.
    thresh_dict = {
            'Origin': pytesseract.image_to_string(roi),
            'M0': pytesseract.image_to_string(morph),
            'T0': pytesseract.image_to_string(thresh),
            }

    return thresh_dict

