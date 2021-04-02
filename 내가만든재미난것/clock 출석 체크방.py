from slacker import Slacker
import datetime
from time import sleep
import random
a=random.randint(1,4)
b=random.randint(1,6)
#file ='C:/Users/701/kdigital/lecture/KakaoTalk_20210107_091516599.jpg'
now = datetime.datetime.now()
slack = Slacker('xoxb-1545617412550-1596845048695-dxAZ4YEFfHEaYLmYlnS1xkPI')
slack.chat.post_message('#출석체크방',"지금은 출석체크할 시간이예요!!!")
slack.chat.post_message('#출석체크방', '안 하신 분들은 얼른 얼른 출석 체크를 해주세요')
sleep(2)
slack.chat.post_message('#출석체크방', 'QR코드를 준비 안 하셨다구요!?!')
slack.chat.post_message('#출석체크방', '제가 미리 준비를 해두었습니다.')
slack.files.upload('C:/Users/701/kdigital/lecture/KakaoTalk_20210107_091516599.jpg', channels='#출석체크방')
slack.chat.post_message('#출석체크방', '얼른 얼른 출석 체크하세요!')
sleep(5)
slack.chat.post_message('#출석체크방','허허 출석 체크 하셔야합니다.')
sleep(10)
slack.chat.post_message('#출석체크방','허허 이러다가 결석처리 됩니다.')
