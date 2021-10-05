import cv2 as cv 
capturaVideo=cv.VideoCapture(0)
if not capturaVideo.isOpened():
    print('No se registro una camara')
    exit()
while True:
    tipocamara,cam=capturaVideo.read() #El subguión es una variable ficticia.
    gris=cv.cvtColor(cam,cv.COLOR_BGR2GRAY)
    cv.imshow('LIVE (PRESS "Q" TO QUIT)', gris)
    if cv.waitKey(1) == ord('q'):#Ord sirve para agregar una tecla de escape en este caso q, de 'quit'
        break
capturaVideo.release()
cv.destroyAllWindows()
