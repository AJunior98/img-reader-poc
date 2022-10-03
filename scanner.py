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

#Variavel de configuração do idioma português no Tesseract
config_tesseract = '--tessdata-dir tessdata' #O PSM é configurado na variável

#Coletando texto da imagem com pytesseract
resultado = pytesseract.image_to_data(rgb, lang='por', config=config_tesseract, output_type=Output.DICT)

#Nível de confiança
min_conf = 40

#Determinando o reconhecimento da imagem
def caixa_texto(resultado, img, cor = (255, 100, 0)):
    x = resultado['left'][i]
    y = resultado['top'][i]
    w = resultado['width'][i]
    h = resultado['height'][i]

    cv2.rectangle(img, (x,y), (x + w, y + h), cor, 2)

    return x, y, img

#Faz a conversão para numpy e adiciona texto na imagem
def escreve_texto(texto, x, y, img, fonte, tamanho_texto=32):
    fonte = ImageFont.truetype(fonte, tamanho_texto)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((x, y - tamanho_texto), texto, font = fonte, fill=(0,0,255,255))
    img = np.array(img_pil)
    return img

#Configuração da saída da imagem
img_copia = rgb.copy()
for i in range(0, len(resultado['text'])):
    confianca = int(resultado['conf'][i])
    if confianca > min_conf:
        x, y, img = caixa_texto(resultado, img_copia)
        texto = resultado['text'][i]
        #cv2.putText(img_copia, texto, (x, y - 10), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.2, (0,0,255))
        img_copia = escreve_texto(texto, x, y, img_copia, fonte)

cv2.imshow('img_copia', img_copia)
cv2.waitKey(0)
cv2.destroyAllWindows()