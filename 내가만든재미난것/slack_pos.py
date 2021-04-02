import pandas as pd
import random
from time import sleep
from slacker import Slacker
pos=pd.read_csv("all_pos.csv",header=0,sep=',')
x= random.randint(0,100)
slack = Slacker('xoxb-1545617412550-1596845048695-dxAZ4YEFfHEaYLmYlnS1xkPI')
slack.chat.post_message('#pos_dic', '오늘 하루도 우리는 건강하고 멋지게 살아야합니다.')
sleep(1)
slack.chat.post_message('#pos_dic', '오늘의 명언:'+pos.loc[x][2]+'은 '+pos.loc[x][1]+'이란 말을 했습니다.')
sleep(1)
slack.chat.post_message('#pos_dic', '그대는 이세상을 아름답게 살아갈 권리가 있습니다.')
sleep(1)
slack.chat.post_message('#pos_dic', '오늘도 화이팅!!!!.')
#print(pos.loc[x][1])#명언
#print(pos.loc[x][2])#사람