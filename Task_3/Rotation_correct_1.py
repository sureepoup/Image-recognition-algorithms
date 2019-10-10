# python 3.7
from PIL import Image
from matplotlib import pyplot as plt
import math
from numpy import matrix
from numpy import linalg


def rot_x(angle, ptx, pty):
    return 1*ptx + 0*pty


def rot_y(angle, ptx, pty):
    return -math.tan(angle/2)*ptx + 1*pty


angle = math.radians(45)
im = Image.open('shrek.jpg')
(x, y) = im.size
xextremes = [rot_x(angle, 0, 0), rot_x(angle, 0, y-1),
             rot_x(angle, x-1,0), rot_x(angle, x-1, y-1)]
yextremes = [rot_y(angle, 0, 0), rot_y(angle, 0, y-1),
             rot_y(angle, x-1, 0), rot_y(angle, x-1, y-1)]
mnx = min(xextremes)
mxx = max(xextremes)
mny = min(yextremes)
mxy = max(yextremes)
Rot_matrix = matrix([[1, 0, -mnx], [-math.tan(angle / 2), 1, -mny], [0, 0, 1]])
Rot_matrix_inv = linalg.inv(Rot_matrix)
Rot_matrix_inv_tuple = (Rot_matrix_inv[0, 0], Rot_matrix_inv[0, 1], Rot_matrix_inv[0, 2],
                        Rot_matrix_inv[1, 0], Rot_matrix_inv[1, 1], Rot_matrix_inv[1, 2])
im1 = im.transform((int(round(mxx-mnx)),int(round((mxy-mny)))),
                   Image.AFFINE, Rot_matrix_inv_tuple, resample=Image.BILINEAR)

def rot_x(angle,ptx,pty):
    return 1*ptx + math.sin(angle)*pty


def rot_y(angle,ptx,pty):
    return 0*ptx + 1*pty


(x,y) = im1.size
xextremes = [rot_x(angle,0,0),rot_x(angle,0,y-1),
             rot_x(angle,x-1,0),rot_x(angle,x-1,y-1)]
yextremes = [rot_y(angle,0,0),rot_y(angle,0,y-1),
             rot_y(angle,x-1,0),rot_y(angle,x-1,y-1)]
mnx = min(xextremes)
mxx = max(xextremes)
mny = min(yextremes)
mxy = max(yextremes)
Rot_matrix = matrix([[1, math.sin(angle), -mnx], [0, 1, -mny], [0, 0, 1]])
Rot_matrix_inv = linalg.inv(Rot_matrix)
Rot_matrix_inv_tuple = (Rot_matrix_inv[0, 0], Rot_matrix_inv[0, 1], Rot_matrix_inv[0, 2],
                        Rot_matrix_inv[1, 0], Rot_matrix_inv[1, 1], Rot_matrix_inv[1, 2])
im2 = im1.transform((int(round(mxx-mnx)),int(round((mxy-mny)))),
                    Image.AFFINE, Rot_matrix_inv_tuple, resample=Image.BILINEAR)


def rot_x(angle,ptx,pty):
    return 1*ptx + 0*pty


def rot_y(angle,ptx,pty):
    return -math.tan(angle/2)*ptx + 1*pty
(x,y) = im2.size
xextremes = [rot_x(angle,0,0),rot_x(angle,0,y-1),
             rot_x(angle,x-1,0),rot_x(angle,x-1,y-1)]
yextremes = [rot_y(angle,0,0),rot_y(angle,0,y-1),
             rot_y(angle,x-1,0),rot_y(angle,x-1,y-1)]
mnx = min(xextremes)
mxx = max(xextremes)
mny = min(yextremes)
mxy = max(yextremes)
Rot_matrix = matrix([[1, 0, -mnx], [-math.tan(angle / 2), 1, -mny], [0, 0, 1]])
Rot_matrix_inv = linalg.inv(Rot_matrix)
Rot_matrix_inv_tuple = (Rot_matrix_inv[0, 0], Rot_matrix_inv[0, 1], Rot_matrix_inv[0, 2],
                        Rot_matrix_inv[1, 0], Rot_matrix_inv[1, 1], Rot_matrix_inv[1, 2])
im3 = im2.transform((int(round(mxx-mnx)),int(round((mxy-mny)))),
                    Image.AFFINE, Rot_matrix_inv_tuple, resample=Image.BILINEAR)


images = [im,im1,im2,im3]
titles = ['Оригинальное изображение', 'Сдвиг строк', 'Сдвиг столбцов', 'Сдвиг строк']
fig = plt.figure(figsize=(18, 16), dpi= 80, facecolor='w', edgecolor='k')

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
