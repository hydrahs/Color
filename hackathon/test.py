from image import *
from PIL import Image
f = Image.open("C:\\Users\\Ruossipha\\Desktop\\20171211224204956.bmp")

f = ImageProcess(f, 0, 'r')
f.save("C:\\Users\\Ruossipha\\Desktop\\3.bmp")