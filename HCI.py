import numpy as np
import cv2
import pytesseract
from PIL import Image
import global_v as GV


def OCR_cap():
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, img = cap.read()
        cv2.rectangle(img,(400,250),(875,525),(0,0,255),10)
        code=""
        cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('p'):
            #image5 = Image.open('000.png')
            cv2.imwrite("123.jpg", img)
            image = Image.open('123.jpg')
            img2 = image.crop((400, 250, 875,500 ))
            #cv2.imwrite("/Users/youjinrui/Desktop/ocr/987.jpg", img2)
            code = pytesseract.image_to_string(img2, lang='chi_tra')
            #code1 = pytesseract.image_to_string(image5, lang='chi_tra')
            img2.show()
            print(code)
            #cv2.imwrite("/Users/youjinrui/Desktop/ocr/321.jpg", img2)
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    GV.text_g=code
    return code