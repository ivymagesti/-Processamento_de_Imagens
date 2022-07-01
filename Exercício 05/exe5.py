import cv2



img = cv2.imread("img-python.jpg")

def getPixel (img, x, y):
    (b,g,r) = img [x,y]

    print('O pixel (', x,', ', y, ') tem as seguintes cores:')
    print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

x = int(input("Digite o valor da posição X: "))
y = int(input("Digite o valor da posição Y: "))

getPixel(img,x,y)

cv2.waitKey(0)