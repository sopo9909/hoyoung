from slacker import Slacker
import datetime
from time import sleep
import random
a=random.randint(0,5)
b=random.randint(0,5)
Off =['강다영','우지원','선생님','황호영','강동아','남윤호','이한비']
dish=['한식','중식','일식','양식','아시아 식','제 3세계 식']
random.shuffle(Off)
now = datetime.datetime.now()
#print(str(now.year),str(now.month),str(now.day),str(now.hour),str(now.minute))
slack = Slacker('xoxb-1545617412550-1596845048695-dxAZ4YEFfHEaYLmYlnS1xkPI')
slack.chat.post_message('#hoho', '사회적 거리두기로 인해...저희도 거리를 둬야합니다...')
slack.chat.post_message('#hoho', '제가 랜덤으로 짝을 뽑아 보았어요')
slack.chat.post_message('#hoho', '1조는 '+Off[0]+","+Off[1]+","+Off[2]+'2조는'+Off[3]+","+Off[4]+","+Off[5]+","+Off[6]+'입니다')
slack.chat.post_message('#hoho', '여러분 오늘은'+str(now.year)+"년"+str(now.month)+"월"+str(now.day)+"일"+str(now.hour)+"시"+str(now.minute)+"분 입니다")
slack.chat.post_message('#hoho', '오늘의 1조 메뉴 종류는 -'+dish[a]+'- 입니다')
slack.chat.post_message('#hoho', '오늘의 2조 메뉴 종류는 -'+dish[b]+'- 입니다')
sleep(2)
slack.chat.post_message('#hoho', Off[0]+' 님 저희의 오늘 식사를 선택해주세요!!')
slack.chat.post_message('#hoho', Off[3]+' 님 저희의 오늘 식사를 선택해주세요!!')
sleep(5)
slack.chat.post_message('#hoho','얼른 정해주세요!')
sleep(10)
slack.chat.post_message('#hoho','왜 아직 정하지 않았나??')
