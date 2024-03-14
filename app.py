from rembg import remove
from PIL import Image

image_file = Image.open(r'.\minha.png')

image_file = image_file.convert('L')

image_file.save(r'.\teste.png')

img = Image.open('minha.png')
img_without_back = remove(img)
img_without_back.save('minha_img.png')

img = Image.open('teste.png')
img_without_back = remove(img)
img_without_back.save('minha_img_cinza.png')