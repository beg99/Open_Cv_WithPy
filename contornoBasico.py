import cv2 as cv
imagen=cv.imread('contorno.jpg')
#GENERAR LA IMAGEN
grises=cv.cvtColor(imagen,cv.COLOR_BGR2GRAY)
_,umbral=cv.threshold(grises, 100,255,cv.THRESH_BINARY)
contorno,jerarquia=cv.findContours(umbral, cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(imagen,contorno,-1,(255, 0, 0), 3) # COLOCANDO (-1) te toma todos los contornos 
#MOSTRAR LA IMAGEN
cv.imshow('imagen', imagen) #IMAGEN ORIGINAL
#cv.imshow('Imagen Gris', grises)# IMAGEN EN GRISES
#cv.imshow('Imagen Umbral',umbral ) 
cv.waitKey(0) # TEMPORIZADOR PARA MOSTRAR VENTANAS EMERGENTES 
cv.destroyAllWindows()
