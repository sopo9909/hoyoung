#%%
from PIL import Image
from PIL import ImageGrab
import matplotlib.pylab as plt
import pyautogui as pag

r =Image.open('C:/Users/701/kdigital/lecture/K_digital_lecture/D0AEcLJVYAErhXl.jpg')
pos = pag.position()
screen = ImageGrab.grab()
color = screen.getpixel(pos)
c_list =[]
c_list.append(color)
m_size = 10
x_m = r.size[0] % m_size
y_m = r.size[1] % m_size
x_p = m_size -x_m
y_p = m_size -y_m
r_new = Image.new(r.mode,(r.size[0]+x_p,r.size[1]+y_p),(255,255,255))
r_new.paste(r,(0,0))
r=r_new
for i in range(0,r.size[0],m_size):
    for j in range(0,r.size[1],m_size):
        r_sum =0
        g_sum =0
        b_sum =0
        for ii in range(i,i+m_size):
            for jj in range(i,j+m_size):
                rgb = r.getpixel((ii,jj))
                r_sum += rgb[0]
                g_sum += rgb[1]
                b_sum += rgb[2]
        r_a = round(r_sum/m_size**2)
        g_a = round(r_sum/m_size**2)
        b_a = round(r_sum/m_size**2)
        rgb_point=[]
        for c in c_list:
            rgb_point.append(abs(r_a-c[0])+abs(g_a-c[1])+abs(b_a-c[2]))
        min_rgb = min(rgb_point)
        min_rgb_ind = rgb_point.index(min_rgb)
        r_f,g_f,b_f =c_list[min_rgb_ind]
        for ii in range(i,i+m_size):
            for jj in range(j,j+m_size):
                r.putpixel((ii,jj),(r_a,g_a,b_a))
plt.imshow(r)
plt.show()
print('끝')
# plt.imshow(r)
# plt.show
# m_size = 10
# x_m = r.size[0] % m_size
# y_m = r.size[1] % m_size
# x_p = m_size -x_m
# y_p = m_size -y_m
# r_new = Image.new(r.mode,(r.size[0]+x_p,r.size[1]+y_p),(255,255,255))
# r_new.paste(r,(0,0))
# r=r_new
# for i in range(0,r.size[0],m_size):
#     for j in range(0,r.size[1],m_size):
#         r_sum =0
#         g_sum =0
#         b_sum =0
#         for ii in range(i,i+m_size):
#             for jj in range(i,j+m_size):
#                 rgb = r.getpixel((ii,jj))
#                 r_sum += rgb[0]
#                 g_sum += rgb[1]
#                 b_sum += rgb[2]
#         r_a = round(r_sum/m_size**2)
#         g_a = round(r_sum/m_size**2)
#         b_a = round(r_sum/m_size**2)
#         for ii in range(i,i+m_size):
#             for jj in range(j,j+m_size):
#                 r.putpixel((ii,jj),(r_a,g_a,b_a))
# plt.imshow(r)
# plt.show()
# print('끝')
# %%
