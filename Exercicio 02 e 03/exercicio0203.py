#Exercício 02 e 03

import cv2 
import numpy as np 

img = cv2.imread("img-python.png")  
cv2.imshow('Imagem Original',img)  

print (f"Altura: {img.shape[0]} pixels") 
print (f"Largura: {img.shape[1]} pixels")
print (f"Canais: {img.shape[2]}")
#print (f"Tamanho: {np.size(img)} bytes") 
 
cv2.waitKey(0) 