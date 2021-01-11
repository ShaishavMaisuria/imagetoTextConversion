from PIL import Image

import pytesseract as pt
pt.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = Image.open(r'picture.jpg')
text=pt.image_to_string(image)

print(text)