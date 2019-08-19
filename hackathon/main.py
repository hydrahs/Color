import voice
import time
from PIL import Image
import math
import numpy as np
import matplotlib.pyplot as plt
from camera import *
from night import Night

du = 1 # 矫正系数
person = voice.Listener()
while True:
    # image = Image.open("C:\\Users\\Ruossipha\\Desktop\\20171211224204956.bmp")
    # showimage(image, 'r', 1 + math.pi / 6)
    #init(1 + math.pi / 6)
    # Camera('r')
    # break
    person.run()  # 说话
    if person.ifrun == 1:
        if person.red == 1:
            method = 'r'
        elif person.green == 1:
            method = 'g'
        elif person.blue == 1:
            method = 'b'
        if person.apply != 1 and (person.red == 1 or person.green == 1 or person.blue == 1):  # 开始调试
            print("开始调试")
            image = Image.open("C:\\Users\\Ruossipha\\Desktop\\20171211224204956.bmp")
            #Camera('r')
            if person.up == 1:
                du += math.pi / 12
                if du > math.pi:
                    du -= math.pi
            elif person.down == 1:
                du -= math.pi / 12
                if du < 0:
                    du += math.pi
            showimage(image, method, du)
            person.up = 0
            person.down = 0
        elif person.apply == 1:  # 打开摄像头，开始后面内容
            init(du)
            print("调试完成")
            Camera(method)
            break
        elif person.night == 1:
            Night()
            break
