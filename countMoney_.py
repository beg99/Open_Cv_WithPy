import cv2 as cv2
import numpy as np 

# UN PEQUEÑO PROGRAMA QUE LEE MONEDAS DE UN PESO Y DOS PESOS ARGENTINA (SOLO LEE DOS MONEDAS, SOBRE UN DIAMETRO DE UNA HOJA A6)
def ordenarPuntos(puntos):
    n_puntos=np.concatenate([puntos[0],puntos[1],puntos[2],puntos[3]]).tolist()
    y_order=sorted(n_puntos,key=lambda n_puntos:n_puntos[1])
    x1_order=y_order[:2]
    x1_order=sorted(x1_order,key=lambda x1_order:x1_order[0])
    x2_order=y_order[2:4]
    x2_order=sorted(x2_order, key=lambda x2_order:x2_order[0])
    return[x1_order[0],x1_order[1],x2_order[0], x2_order[1]]


def aliniar(imagen, ancho, alto):
    imagen_alineada=None
    gris=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    _,umbral=cv2.threshold(gris,150,255, cv2.THRESH_BINARY)
    #cv2.imshow('umbral', umbral)
    contorno=cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contorno=sorted(contorno,key=cv2.contourArea, reverse=True)[:1]
    for c in contorno:
        epilson=0.01*cv2.arcLength(c, True)
        approx=cv2.approxPolyDP(c, epilson, True)
        if len(approx)== 4:
            puntos=ordenarPuntos(approx)
            puntos1=np.float32(puntos)
            puntos2=np.float32([[0,0],[ancho,0],[0,alto],[ancho,alto]])
            fijo= cv2.getPerspectiveTransform(puntos1,puntos2)
            imagen_alineada=cv2.warpPerspective(imagen, fijo, (ancho,alto))
    return imagen_alineada
##CAPTURA DE VIDEO
capturavideo= cv2.VideoCapture(0)


while True:
    tipocamara,cam=capturavideo.read()
    if tipocamara== False:
        break
    imagen_a6=aliniar(cam,ancho=480, alto=677)
    if imagen_a6 is not None:
        puntos=[]
        imagen_gris=cv2.cvtColor(imagen_a6,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(imagen_gris,(5,5),1)
        _,umbral2=cv2.threshold(blur,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)
        #cv2.imshow('umbral', umbral2)
        contorno2= cv2.findContours(umbral2,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(imagen_a6, contorno2, -1, (255,0,0), 2)
        suma1=0.0
        suma2=0.0
        for c_2 in contorno2:
            area=cv2.contourArea(c_2)
            momentos = cv2.moments(c_2)
            if(momentos["m00"]==0):
                momentos["m00"]=1.0
            x=int(momentos["m10"]/ momentos["m00"])
            y=int(momentos["m01"]/momentos["m00"])
            
            if area< 7400 and area > 7000:
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_a6,'$2 PESOS',(x,y), font, 0.75, (0,255,0), 2)
    
            if area< 6700 and area > 6900:
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_a6,'$1 PESO',(x,y), font, 0.75, (0,255,0), 2)
              
        cv2.imshow('Imagen A6, PRESS "Q" TO QUIT', imagen_a6)
        #cv2.imshow('Camara', cam)
        if cv2.waitKey(1) == ord('q'):
            break
capturavideo.release()
cv2.destroyAllWindows()
