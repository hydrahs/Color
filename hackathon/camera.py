import numpy as np
import cv2
from image import *
import matplotlib.pyplot as plt


def showimage(image, mo, du):
    plt.figure()
    plt.subplot(2, 2, 1)
    # plt.figure()
    plt.imshow(image)
    blind = ImageProcess(image, 0, mo)
    # plt.figure()
    plt.subplot(2, 2, 2)
    plt.imshow(blind)
    # plt.figure()
    cor = Correct2(image,du)
    plt.subplot(2, 2, 3)
    plt.imshow(cor)
    # plt.figure()
    bcor = ImageProcess(cor, 0, mo)
    plt.subplot(2, 2, 4)
    plt.imshow(bcor)
    plt.show()


def PicChange(frame, method):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = Image.fromarray(frame)
    frame = ImageProcess(frame, 0, method)
    frame = np.array(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    return frame


def Camera(method):
    cap = cv2.VideoCapture(0)  # 从摄像头中取得视频
    cap.set(3,160) #设置分辨率
    cap.set(4,120)
    # 获取视频播放界面长宽
    # width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    # height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)

    # # 定义编码器 创建 VideoWriter 对象
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Be sure to use the lower case
    # norm = cv2.VideoWriter('norm.mp4', fourcc, 20.0, (width, height))
    # blind = cv2.VideoWriter('blind.mp4', fourcc, 20.0, (width, height))
    # correct = cv2.VideoWriter('correct.mp4', fourcc, 20.0, (width, height))
    # norm_correct = cv2.VideoWriter('norm_correct.mp4', fourcc, 20.0, (width, height))
    while(cap.isOpened()):
        # 读取帧摄像头
        ret, frame = cap.read()
        if ret == True:
            # 输出当前帧
            # norm.write(frame)
            cv2.imshow('Camera', frame)
            blindf = PicChange(frame, method)
            # blind.write(blindf)
            cv2.imshow('BlindCamera', blindf)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            corf = Correct(Image.fromarray(frame))
            corf = cv2.cvtColor(np.array(corf),cv2.COLOR_RGB2BGR)
            # correct.write(corf)
            cv2.imshow('CorCamera', corf)
            bcorf = PicChange(corf, method)
            # norm_correct.write(bcorf)
            cv2.imshow('BCor', bcorf)
            # 键盘按 q 退出
            if (cv2.waitKey(50) & 0xFF) == ord('q'):
                break
        else:
            break
    # 释放资源

    cap.release()
    cv2.destroyAllWindows()
