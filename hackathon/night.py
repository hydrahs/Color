import matplotlib.pyplot as plt
import pylab
import cv2
import numpy as np

def Night():
    img = plt.imread("2.jpg")                        #在这里读取图片
    plt.imshow(img)                                     #显示读取的图片
    fil = np.array([[ 0, 0, 0],                        #这个是设置的滤波，也就是卷积核
                    [ 2, 0, 2],
                    [ 0, 0, 0]])
    res = cv2.filter2D(img, -1, fil)  #使用opencv的卷积函数
    plt.subplot(1, 2, 1)
    plt.title('original picture')
    plt.imshow(img)
    plt.axis('off')  #不显示坐标尺寸
    
    plt.subplot(1, 2, 2)
    plt.title('night mode')
    plt.imshow(res)  #显示卷积后的图片
    plt.axis('off')  #不显示坐标尺寸
    
    plt.show()   #显示窗口