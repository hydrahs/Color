import middle
import time
from PIL import Image
import math
import numpy as np
import matplotlib.pyplot as plt
from camera import *

du = 1 # 矫正系数
# person = middle.Listener()

while True:
    # person.run()  # 说话
    # if person.ifrun == 1:
    #     if person.red == 1:
    #         method = 'r'
    #     elif person.green == 1:
    #         method = 'g'
    #     elif person.blue == 1:
    #         method = 'b'
    # if person.apply != 1 and (person.red == 1 or person.green == 1 or person.blue == 1):  # 开始调试
        print("开始调试")
        image = Image.open("C:\\Users\\Ruossipha\\Desktop\\20171211224204956.bmp")
        #showimage(image,'r',du)