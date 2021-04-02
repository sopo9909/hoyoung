<<<<<<< HEAD
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pylab as plt
import copy
import random
target = Image.open(r'C:/Users/701/Pictures/[꾸미기]D0AEcLJVYAErhXl.jpg')
model = Image.new(target.mode,target.size)
k = 0
while 1 :
    if k < 300:
        font_size = random.randrange(20,60)
    else:
        font_size = random.randrange(0,20)
    font_position_x = random.randrange(-model.size[0],model.size[0])
    font_position_y = random.randrange(-model.size[1],model.size[1])
    text = 'IU'
    rgb_target = target.convert('RGB') #타겟의 RGB를 가져온다
    r,g,b = rgb_target.getpixel((random.randrange(0,model.size[0]),random.randrange(0,model.size[1]))) #타겟의 RGB
    font  = ImageFont.truetype('arial.ttf',font_size)
    new_model = copy.deepcopy(model)
    draw = ImageDraw.Draw(new_model)
    draw.text((font_position_x,font_position_y),text,(r,g,b),font=font)
    rgb_model = model.convert('RGB')
    rgb_new_model = new_model.convert('RGB')
    point_model = 0
    point_new_model = 0
    for i in range(0,target.size[0]):
        for j in range(0,target.size[1]):
            r0,g0,b0 = rgb_model.getpixel((i,j))
            r1,g1,b1 = rgb_new_model.getpixel((i,j))
            rt,gt,bt = rgb_target.getpixel((i,j))
            point_model += abs(rt-r0)+abs(gt-g0)+abs(bt-b0)
            point_new_model += abs(rt-r1)+abs(gt-g1)+abs(bt-b1)
    if point_new_model < point_model:
        model = new_model
        k +=1
        model.save('IU/model_{}.jpg'.format(k))
=======
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pylab as plt
import copy
import random
target = Image.open(r'C:/Users/701/Pictures/[꾸미기]D0AEcLJVYAErhXl.jpg')
model = Image.new(target.mode,target.size)
k = 0
while 1 :
    if k < 300:
        font_size = random.randrange(20,60)
    else:
        font_size = random.randrange(0,20)
    font_position_x = random.randrange(-model.size[0],model.size[0])
    font_position_y = random.randrange(-model.size[1],model.size[1])
    text = 'IU'
    rgb_target = target.convert('RGB') #타겟의 RGB를 가져온다
    r,g,b = rgb_target.getpixel((random.randrange(0,model.size[0]),random.randrange(0,model.size[1]))) #타겟의 RGB
    font  = ImageFont.truetype('arial.ttf',font_size)
    new_model = copy.deepcopy(model)
    draw = ImageDraw.Draw(new_model)
    draw.text((font_position_x,font_position_y),text,(r,g,b),font=font)
    rgb_model = model.convert('RGB')
    rgb_new_model = new_model.convert('RGB')
    point_model = 0
    point_new_model = 0
    for i in range(0,target.size[0]):
        for j in range(0,target.size[1]):
            r0,g0,b0 = rgb_model.getpixel((i,j))
            r1,g1,b1 = rgb_new_model.getpixel((i,j))
            rt,gt,bt = rgb_target.getpixel((i,j))
            point_model += abs(rt-r0)+abs(gt-g0)+abs(bt-b0)
            point_new_model += abs(rt-r1)+abs(gt-g1)+abs(bt-b1)
    if point_new_model < point_model:
        model = new_model
        k +=1
        model.save('IU/model_{}.jpg'.format(k))
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
        print(k)