from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math

tab1 = np.zeros((256, 256, 256))
tab2 = np.zeros((256, 256, 256))
tab3 = np.zeros((256, 256, 256))
eps = 1e-6

def ImageProcess(image, lamda, method):
    # image图片对象，lamda参数，method色盲模式
    r, g, b = image.split()
    mr = np.array(r)
    mg = np.array(g)
    mb = np.array(b)
    if method == 'r':
        Method1 = mr * ((lamda + 0.1628) / (1 + 0.1628)) + mg * ((1 - lamda) / (1 + 0.1628))
        Method2 = mr * +((0.1628 * (1 - lamda)) / (1 + 0.1628)) + mg * (((1 - lamda) / (1 + 0.1628)) + lamda)
        Method3 = mb
    elif method == 'g':
        Method1 = mr * ((lamda + 0.4945) / (1 + 0.4945)) + mg * ((1 - lamda) / (1 + 0.4945))
        Method2 = mr * ((0.4945 * (1 - lamda)) / (1 + 0.4945)) + mg * (((1 - lamda) / (1 + 0.4945)) + lamda)
        Method3 = mb
    elif method == 'b':
        Method1 = mr * 1.03 + mg * 0.144 - mb * 0.144
        Method2 = mg * ((lamda + 6.136) / (1 + 6.136)) + mb * ((1 - lamda) / (1 + 6.136))
        Method3 = mg * ((6.136 * (1 - lamda)) / (1 + 6.136)) + mb * (((1 - lamda) / (1 + 6.136)) + lamda)
        # print(Method1 == mr)
        # print(Method2 == mg)
        # print(Method3 == mb)
    r2 = Image.fromarray(Method1).convert('L')
    g2 = Image.fromarray(Method2).convert('L')
    b2 = Image.fromarray(Method3).convert('L')
    image2 = Image.merge("RGB", (r2, g2, b2))
    return image2
    # print(data[100,100])
    # new_im = MatrixToImage(data)
    # plt.imshow(data)
    # new_im.show()
    # new_im.save("C:\\Users\\Ruossipha\\Desktop\\2017.bmp")
# image = Image.open('C:\\Users\\Ruossipha\\Desktop\\20171211224204956.bmp')
# image2=ImageProcess(image, 1, 'b')
# plt.imshow(image2)
# plt.show()
def init(du):
    for i in range(0, 256):
        print(i)
        for j in range(0, 256):
            for k in range(0, 256):
                mr = i / 255
                mg = j / 255
                mb = k / 255
                num1 = 0.5 * ((mr - mg) + (mr - mb))
                den = math.sqrt((mr - mg) ** 2 + (mr - mb) * (mg - mb))
                theta = math.acos(num1 / (den + eps))
                H = theta
                den = mr + mg + mb
                if (den == 0):
                    den = eps
                num = mr
                if (num > mg):
                    num = mg
                if (num > mb):
                    num = mb
                if (mb > mg):
                    H = 2 * math.pi - H
                if (den == 0):
                    den = eps
                S = 1 - 3 * num / den
                if (S == 0):
                    H = 0
                I = (mr + mg + mb) / 3
                H = H + du
                if (H > 2 * math.pi):
                    H -= 2 * math.pi
                if (H >= 0 and H < 2 * math.pi / 3):
                    B = I * (1 - S)
                    R = I * (1 + S * math.cos(H) / math.cos(math.pi / 3 - H))
                    G = 3 * I - (R + B)
                elif (H >= 2*math.pi/3 and H < 4 * math.pi / 3):
                    R = I * (1 - S)
                    G = I * (1 + S * math.cos(H - 2 * math.pi / 3) / math.cos(math.pi - H))
                    B = 3 * I - (R + G)    
                else:
                    G = I * (1 - S)
                    B = I * (1 + S * math.cos(H - 4 * math.pi / 3) / math.cos(5 * math.pi / 3 - H))
                    R = 3 * I - (G + B)
                tab1[i][j][k] = R
                tab2[i][j][k] = G
                tab3[i][j][k] = B
                
def Correct(rgb):
    r, g, b = rgb.split()
    mr = np.array(r)
    mg = np.array(g)
    mb = np.array(b)
    a,b=mr.shape
    R = np.zeros((a, b))
    G = np.zeros((a, b))
    B = np.zeros((a, b))
    for i in range(0, a):
        for j in range(0, b):
            R[i, j] = tab1[mr[i, j]][mg[i, j]][mb[i, j]]
            G[i, j] = tab2[mr[i, j]][mg[i, j]][mb[i, j]]
            B[i, j] = tab3[mr[i, j]][mg[i, j]][mb[i, j]]
    r2 = Image.fromarray(R*255).convert('L')
    g2 = Image.fromarray(G*255).convert('L')
    b2 = Image.fromarray(B*255).convert('L')
    image2 = Image.merge("RGB", (r2, g2, b2))
    return image2

def Correct2(rgb, du):
    eps = 1e-6
    r, g, b = rgb.split()
    mr = np.array(r)/255
    mg = np.array(g)/255
    mb = np.array(b)/255
    a,b=mr.shape
    num1 = 0.5 * ((mr - mg) + (mr - mb))
    den = np.zeros((a, b))
    theta = np.zeros((a, b))
    num = np.ones((a, b))
    R = np.zeros((a, b))
    G = np.zeros((a, b))
    B = np.zeros((a, b))
    H = np.zeros((a, b))
    S = np.zeros((a, b))
    I = np.zeros((a, b))
    for i in range(0, a):
        for j in range(0, b):
            den[i, j] = math.sqrt((mr[i, j] - mg[i, j]) ** 2 + (mr[i, j] - mb[i, j]) * (mg[i, j] - mb[i, j]))
            theta[i, j] = math.acos(num1[i, j] / (den[i, j] + eps))
            H[i,j] = theta[i,j]
            den[i,j] = mr[i,j] + mg[i,j] + mb[i,j]
            if (den[i, j] == 0):
                den[i, j] = eps
            if (num[i,j] > mr[i, j]):
                num[i,j] = mr[i, j]
            if (num[i,j] > mg[i, j]):
                num[i,j] = mg[i, j]
            if (num[i,j] > mb[i, j]):
                num[i,j] = mb[i, j]
            if (mb[i, j] > mg[i, j]):
                H[i, j] = 2 * math.pi - H[i, j]
            if (den[i, j] == 0):
                den[i, j] = eps
            S[i,j] = 1 - 3 * num[i,j] / den[i,j]
            if (S[i][j] == 0):
                H[i][j] = 0
            I[i,j] = (mr[i,j] + mg[i,j] + mb[i,j]) / 3
            H[i,j] = H[i,j] + du
            if (H[i, j] > 2 * math.pi):
                H[i, j] -= 2 * math.pi
            if (H[i, j] >= 0 and H[i, j] < 2 * math.pi / 3):
                B[i, j] = I[i, j] * (1 - S[i, j])
                R[i, j] = I[i, j] * (1 + S[i, j] * math.cos(H[i, j]) / math.cos(math.pi / 3 - H[i, j]))
                G[i, j] = 3 * I[i, j] - (R[i, j] + B[i, j])
            elif (H[i, j] >= 2*math.pi/3 and H[i, j] < 4 * math.pi / 3):
                R[i, j] = I[i, j] * (1 - S[i, j])
                G[i, j] = I[i, j] * (1 + S[i, j] * math.cos(H[i, j] - 2 * math.pi / 3) / math.cos(math.pi - H[i, j]))
                B[i, j] = 3 * I[i, j] - (R[i, j] + G[i, j])    
            else:
                G[i, j] = I[i, j] * (1 - S[i, j])
                B[i, j] = I[i, j] * (1 + S[i, j] * math.cos(H[i, j] - 4 * math.pi / 3) / math.cos(5 * math.pi / 3 - H[i, j]))
                R[i, j] = 3 * I[i, j] - (G[i, j] + B[i, j])
    r2 = Image.fromarray(R*255).convert('L')
    g2 = Image.fromarray(G*255).convert('L')
    b2 = Image.fromarray(B*255).convert('L')
    image2 = Image.merge("RGB", (r2, g2, b2))
    return image2