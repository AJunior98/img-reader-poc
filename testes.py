import pytesseract
import cv2 # OpenCV
import numpy as np
from PIL import ImageFont, Image, ImageDraw
from pytesseract import Output

#Caminho da imagem
img = cv2.imread('imagens\Capturar.PNG')

#Definindo a fonte do projeto
fonte = 'fontes\calibri.ttf'

#Formatando imagem de BGR para RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()