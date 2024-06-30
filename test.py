import cv2

webc = cv2.VideoCapture(1)

def webcc():
    if not webc.isOpened():
        print("Error")
        exit()
    path = 'webcam.jpg'
    ret = webc.read()
    frame = webc.read()
    cv2.imwrite(path, frame)

webcc()