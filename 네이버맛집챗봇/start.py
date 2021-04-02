# -*- coding: utf-8 -*-
from slacker import Slacker
import datetime
from time import sleep
import random
from flask import Flask, request, make_response
import json
#슬랙이 사용자에게 말을 검
slack = Slacker('xoxb-1545617412550-1596845048695-dxAZ4YEFfHEaYLmYlnS1xkPI') # 슬랙의 토큰을 입력한다.
slack.chat.post_message('#hoho', '사회적 거리두기로 인해...저희도 거리를 둬야합니다...') # 채널 명과 함께 메시지를 보낸다.
app = Flask(__name__)
#사용자가 슬랙에게 답을 함 - 한,중,일,양
dish=['한식','중식','일식','양식','아시아 식','제 3세계 식']
slack.chat.post_message('#hoho', '오늘의 1조 메뉴 종류를 '+dish+'에서 정해주세요.')
def get_answer():
    return "hello"
def event_handler(event_type,slack_event):
    if event_type =="app_mention":
        channel = slack_event["event"]["channel"]
        text = get_answer
        slack.chat.post_message(channel,text)
        return make_response("앱 멘션 메시지가 보내졌습니다.",200,)
    message = "[%s] 에빈트 핸들러를 찾을 수 없습니다."%event_type
    return make_response(message,200,{"X-Slack-No-Retry":1})
@app.route("/slack",methods=["GET","POST"])
def hears():
    slack_event = json.loads(request.data)
    if "challenge" in slack_event:
     return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})

    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return event_handler(event_type, slack_event)
    return make_response("슬랙 요청에 이벤트가 없습니다.", 404, {"X-Slack-No-Retry": 1})

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)
#슬랙이 사용자에게 추천을 함 - 이런 집이 있다.

a=random.randint(0,5)
b=random.randint(0,5)
Off =['강다영','우지원','김광희','황호영','윤현수']
random.shuffle(Off)
now = datetime.datetime.now()
#print(str(now.year),str(now.month),str(now.day),str(now.hour),str(now.minute))
slack.chat.post_message('#hoho', '사회적 거리두기로 인해...저희도 거리를 둬야합니다...')
slack.chat.post_message('#hoho', '제가 랜덤으로 짝을 뽑아 보았어요')
slack.chat.post_message('#hoho', '1조는 '+Off[0]+","+Off[1]+'2조는'+Off[2]+","+Off[3]+","+Off[4]+'입니다')
slack.chat.post_message('#hoho', '여러분 오늘은'+str(now.year)+"년"+str(now.month)+"월"+str(now.day)+"일"+str(now.hour)+"시"+str(now.minute)+"분 입니다")
slack.chat.post_message('#hoho', '오늘의 1조 메뉴 종류는 -'+dish[a]+'- 입니다')
slack.chat.post_message('#hoho', '오늘의 2조 메뉴 종류는 -'+dish[b]+'- 입니다')
sleep(2)
slack.chat.post_message('#hoho', Off[0]+' 님 저희의 오늘 식사를 선택해주세요!!')
slack.chat.post_message('#hoho', Off[2]+' 님 저희의 오늘 식사를 선택해주세요!!')
sleep(5)
slack.chat.post_message('#hoho','얼른 정해주세요!')
sleep(10)
slack.chat.post_message('#hoho','왜 아직 정하지 않았나??')
