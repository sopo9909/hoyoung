#%%
from PIL import Image
from PIL import ImageGrab
import matplotlib.pylab as plt
import pyautogui as pag
import PIL.Image as pilimg
import numpy as np
import cv2
mode = True
drawing = False
ix, iy = -1, -1
#img =pilimg.open('C:/Users/701/kdigital/lecture/K_digital_lecture/D0AEcLJVYAErhXl.jpg')
# Input image
input = cv2.imread('C:/Users/701/kdigital/lecture/K_digital_lecture/D0AEcLJVYAErhXl.jpg')
# # Get input size
# width, height, _ = input.shape
# # Desired "pixelated" size
# w, h = (120, 120)
# #이미지 흑백으로
# input1 =cv2.cvtColor(input,cv2.COLOR_BGR2GRAY)
# # Resize input to "pixelated" size
# temp = cv2.resize(input1, (w, h), interpolation=cv2.INTER_LINEAR)
# # Initialize output image
# output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
# cv2.imshow('Input', input)
# cv2.imshow('Output', output)
# cv2.waitKey(0)
def mosaic(input,ratio=0.01):
    small = cv2.resize(input,None, fx=ratio,fy=ratio,interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, input.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
dst_01 = mosaic(input)
cv2.imwrite('C:/Users/701/kdigital/lecture/K_digital_lecture/D0AEcLJVYAErhXl1.jpg', dst_01)
img = cv2.imread('C:/Users/701/kdigital/lecture/K_digital_lecture/D0AEcLJVYAErhXl1.jpg')
cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.waitKey(0)

def mosaic_area(input, x, y, width, height, ratio=0.1):
    dst = src.copy()
    dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
    return dst


dst_area = mosaic_area(src, 270, 130, 150, 60)


#cv2.setMouseCallback('image',draw_pixel)
# def draw_pixel(event, x, y, flags, param):
#     global ix, iy, drawing, mode
#     if event == cv2.EVENT_LBUTTONDOWN:
#         #누르는 것 = 
#         drawing = True
#         ix, iy = x, y

#     elif event == cv2.EVENT_MOUSEMOVE:
#         #움직임
#         if drawing == True:
#             if mode == True:
#                 cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
#             else:
#                 cv2.circle(img, (x,y), 5, (0,0,255), -1)

#     elif event == cv2.EVENT_LBUTTONUP:
#         #땐다
#         drawing = False
#         if mode == True:
#             cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
#         else:
#             cv2.circle(img, (x,y), 5, (0,0,255), -1)

# img = cv2.imread('C:/Users/701/kdigital/lecture/K_digital_lecture/D0AEcLJVYAErhXl.jpg')
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_pixel)



# %%
