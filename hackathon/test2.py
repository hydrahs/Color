import numpy as np
import cv2

class getImag:
    def __init__(self):

        self.cap=cv2.VideoCapture(0)
        self.cap.isOpened()
        self.r=0
        self.frame = cv2.imread('text.jpg')

    def run2(self):

        while True:
            ret,self.frame = self.cap.read()
            self.r = self.r + 500 
            #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            if self.r%1000==0:
                cv2.imshow('hello',self.frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        self.cap.release()
        cv2.destroyAllWindows()