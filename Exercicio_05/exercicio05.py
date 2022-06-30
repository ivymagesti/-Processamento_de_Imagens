import cv2

posx = int(input("Digite o valor da posição X: "))
largura = int(input("Digite o valor da Largura: "))
posy = int(input("Digite o valor da posição Y: "))
altura = int(input("Digite o valor da Altura: "))

img = cv2.imread("img-python.png")
cv2.imshow("Original", img)

img_modificada = img
img_modificada[posx:largura, posy:altura] = (0, 0, 0) 

cv2.imshow("Modificada", img_modificada) 

cv2.imwrite("Img-Modificada.png", img_modificada) 
cv2.waitKey(0)
