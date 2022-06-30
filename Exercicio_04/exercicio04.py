# Exercício - 04

import numpy as np
import cv2

# Posição x e y do pixel a ser retornado
POSI_X = 300
POSI_Y = 200

def getPixel(image,posiX, posiY):
    return image[posiX][posiY]
    


def main():
    img = cv2.imread("lontra.png")
    posiX = int(input("Digite a posicao X do PIXEL: "))
    posiY = int(input("Digite a posicao Y do PIXEL: "))

    valor = getPixel(img,posiX, posiY)
    print("RBG Pixel: " , valor)
main()