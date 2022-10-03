## Bibliotecas utilizadas

pip install numpy opencv-contrib-python
pip install pytesseract
pip install pillow scipy
pip install scikit-learn scikit-image
pip install imutils matplotlib
pip install requests beautifulsoup4
pip install h5py tensorflow textblob
Todas as libs acima foram coletadas do site: https://pyimagesearch.com/2021/08/16/installing-tesseract-pytesseract-and-python-ocr-packages-on-your-system/

# Instalação do Tesseract
Obs: Como o Tesseract não tem suporte para o Windows, é preciso fazer o download de um .exe para que consigamos seguir adiante, link abaixo:
Fonte do manual: https://www.projectpro.io/article/how-to-train-tesseract-ocr-python/561#:~:text=and%20Mac%20machines%20%2D-,How%20to%20install%20Tesseract%20OCR%20in%20Python%20on%20Windows%3F,path%20to%20your%20environment%20variables.

Tesseract.exe: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.2.0.20220712.exe

Após isso, adicionar as variáveis de ambiente o caminho onde seu Tesseract foi instalado.

# Observações
Quando é carregada uma imagem no OpenCV, automaticamente ela passará para o formato BGR e precisamos converter para o RGB.

# Page segmentation modes
Essa ferramenta da opções de como podemos tratar a imagem coletada no texto, para conseguir acessar as opções, cole o comando a seguir: tesseract --help-psm
Obs: O PSM tem que ser configurado diretamente na variável de configuração do tesseract. O mais indicado é utilizar o padrão 6.

