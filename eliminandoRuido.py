from cv2 import cv2 as cv 
import numpy as np 
##TURN INTO GREEN##
def contadorMonedas():
    gaussX=3# AL ENFOQUE GAUSS HAY QUE DARLE UNA MATRIX EJEMPLO  3X3 Y TIENEN QUE SER IMPARES
    kernelV=3
    autentic= cv.imread('monedas.jpg')
    greyV=cv.cvtColor(autentic,cv.COLOR_BGR2GRAY)
    gB=cv.GaussianBlur(greyV,(gaussX,gaussX), 0 )# RECOMENDACION DE DOC DAR EL ULTIMO VALOR =
    canny= cv.Canny(gB,60,100)
    ##NUMPY##
    kernel=np.ones((kernelV,kernelV),np.uint8) 
    cierre= cv.morphologyEx(canny, cv.MORPH_CLOSE, kernel)
    contorno,jerarquia=cv.findContours(cierre.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    ##COUNT##
    print('Monedas encontradas: {}'.format(len(contorno)))
    cv.drawContours(autentic, contorno, -1, (0, 0, 255),1)
    ##SHOW##
    #cv.imshow('Imagen', autentic)
    #cv.imshow('Gris', greyV)
    #cv.imshow('Gauss', gB)
    #cv.imshow('Canny', canny)
    cv.imshow('RESULTADO', autentic)
    cv.waitKey(0)
    cv.destroyAllWindows()  

contadorMonedas()