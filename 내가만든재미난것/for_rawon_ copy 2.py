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
#이미지를 넣음
input = cv2.imread('C:/Users/701/kdigital/lecture/K_digital_lecture/D0AEcLJVYAErhXl.jpg')
cv2.namedWindow('image')
def mosaic(input,ratio=0.01):
    small = cv2.resize(input,None, fx=ratio,fy=ratio,interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, input.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
img = mosaic(input)
#첫번째 이미지를 변환했음
#cv2.imwrite('C:/Users/701/kdigital/lecture/K_digital_lecture/D0AEcLJVYAErhXl1.jpg', dst_01)
#img = cv2.imread('C:/Users/701/kdigital/lecture/K_digital_lecture/D0AEcLJVYAErhXl1.jpg')
#img가 모자이크화된 이미지다.
#cv2.imshow('image', img)
#cv2.waitKey(0)

def mosaic_area(img, x, y, width, height, ratio=0.1):
    dst = img.copy()
    dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
    return dst

def draw_pixel(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        #누르는 것 = 
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        #움직임
        if drawing == True:
            mosaic_area(img,x,y,10,10)
    elif event == cv2.EVENT_LBUTTONUP:
        #땐다
        drawing = False
cv2.setMouseCallback('image',draw_pixel)
#dst_area = mosaic_area(img, 270, 130, 150, 60)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()

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
