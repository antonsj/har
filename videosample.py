cam = cv2.VideoCapture(sourceVideo)            
while True:
    ret, img = cam.read()                      
    cv2.imshow('detection', img)
    print ret
    if (0xFF & cv2.waitKey(5) == 27) or img.size == 0:
        break
