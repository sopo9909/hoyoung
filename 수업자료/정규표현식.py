<<<<<<< HEAD

# -*- coding: utf-8 -*-
import re
text = '''
전국 언론 노동자들이 시민사회단체와 함께 네이버의 지역 차별을 규탄하고 개선을 촉구하는 무기한 릴레이 시위에 돌입했다.

전국언론노조와 전국 민주언론시민연합(민언련)은 1일 오전 11시 30분 경기도 성남시의 네이버 본사(그린팩토리) 앞에서 1인 시위를 시작했다. 이날 시위에는 오정훈 전국언론노동조합위원장, 전대식 지역신문노동조합협의회 의장(부산일보 지부장), 김명래 경인일보지부장, 민진영 경기민주언론시민연합 사무처장 등이 참여했다.

이들은 1인 시위를 통해 ‘네이버 뉴스 서비스 지역 언론 배제 개선’을 요구하고 ‘지역 공론장 형성을 위한 네이버의 공적 책임’을 촉구했다. 전국언론노조와 민언련은 매주 월요일마다 네이버 본사 앞 시위를 진행할 예정이다.

네이버는 최근 뉴스 서비스에 인공지능 에어스(AiRS) 알고리즘을 적용하는 방식으로 뉴스 편집 기능을 개편했다. 이후 지역 언론사 뉴스의 노출이 현격하게 줄어들었다. 아울러 100여 개 모바일 콘텐츠 제휴 언론사 중 독자가 구독을 선택할 수 있는 ‘채널’ 제휴사 44곳을 선정했는데 이 과정에서 지역 언론을 철저하게 배제했다. 이에 반발해 전국언론노조뿐 아니라 한국지방신문협회, 대한민국지방신문협의회 등 지역 신문 단체도 공동 성명을 발표하며 개선을 요구하고 나섰다. 전국시도의회의장협의회는 최근 총회에서 ‘네이버 지역 언론 배제 반대 성명’을 채택하기도 했다. 하지만 이 같은 반발에도 네이버는 뚜렷한 해결책을 내지 않고 있다.

오정훈 위원장은 1인 시위에서 “네이버는 해결책을 내놓기는커녕 뉴스제휴평가위원회에만 책임을 떠넘기고 있다”며 “지역 언론 배제 문제의 해결을 위한 대화 요구에 즉각 응답해 뉴스 유통사업자로서의 사회적 역할을 수행해야 한다”고 촉구했다.

전대식 의장은 “2005년 당시 네이버는 모든 언론사에 뉴스 유통망을 제공하는 우군이었지만 15년 만에 갑질하고 횡포하는 기업으로 전락했다”며 “지역 언론 종사자들이 만든 콘텐츠가 네이버에서 사라진 현실을 놓고 대화하고 상생적으로 풀어야 한다”면서 협의 창구 개설을 요구했다.

민언련은 국내 1위 포털 네이버가 지역 공론장을 만드는 사회적 책임을 외면하는 것은 현 정부의 지방분권 강화 정책에 위배되는 것이라고 지적했다.

민진영 사무처장은 “네이버가 지역신문에 대한 보도를 배제하고 시민들과의 소통 창구를 차단하는 것은 현 정부 정책인 지방분권 강화, 민주주의 정착이라는 큰 의제를 거역하는 것”이라며 “이런 행태는 반드시 중단돼야 하고 다양한 소식들이 소비자와 시민에게 전달돼야 한다”고 강조했다.

출처 : 제주新보(http://www.jejunews.com) 
'''
result = re.findall("네이버",str(text))
print(result)

numbers = """
010-2334-3234
02-302-3033
010-1321-4043
02-01-32
33-3303-3033
016-444-3042
"""

result2 = re.findall("\d{3}-\d{3,4}-\d{4}",numbers)
result3 = re.findall("0\d{1,2}-\d{3,4}-\d{4}",numbers)
print(result2)
print(result3)

email ="""
jkilee@gmail.com
kttredef@naver.com
akdef!aa.com
adekik@best.kr
abkereff@aacde
adefgree@korea.co.kr
"""
result4 = re.findall("\w+@\w+\.\w+\.?\w*",email)
print(result4)

text2 ="""
안녕하세요 저는 <em>홍길동</em> 입니다. 나이는 24살 세계 최고의 <a href="aa.aa.com">데이터 분석가</a>가 되고싶습니다.

"""
result5 = re.sub("<[^<]*>","",text2)
print(result5)

text3 ="""<p>
<span>네이버가 뉴스 서비스에 인공지능(AI)을 도입해 페이지 뷰(PV)를 늘리고 이용자를 끌어 모으고 있다.</span>
<span>네이버는 5일 오전 서울 강남구 그랜드 인터컨티넨털 호텔에서 AI 콜로키움 2019를 열고 이 같은 AI 성과와 전략을 소개했다.</span>
<span>이날 기조연설에서 김광현 네이버 서치앤클로바 리더는 "AI 뉴스 추천 시스템인 에어스(AiRS)를 도입하면서 뉴스 소비량이 확대되고 있다" 고 말했다.</span>
</p>"""
result6 = re.findall("<[^<]*>.*<[^<]*>",text3)
result7=[]
for i in range(len(result6)):
    result7.append(re.sub("<[^<]*>","",result6[i]))
print(result7)

rrmrm = re.findall(r'(?<=<span>).+(?=</span)',text3)
print(rrmrm)
import requests
from bs4 import BeautifulSoup

URL= 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
result = soup.select(".list_ranking tr > td.title a")
for i, v in enumerate(result):
    print(i+1, v.text)

URL= 'https://finance.naver.com/sise/sise_quant.nhn'
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
result = soup.select(".box_type_1 tr > td.title a")
for i, v in enumerate(result):
=======

# -*- coding: utf-8 -*-
import re
text = '''
전국 언론 노동자들이 시민사회단체와 함께 네이버의 지역 차별을 규탄하고 개선을 촉구하는 무기한 릴레이 시위에 돌입했다.

전국언론노조와 전국 민주언론시민연합(민언련)은 1일 오전 11시 30분 경기도 성남시의 네이버 본사(그린팩토리) 앞에서 1인 시위를 시작했다. 이날 시위에는 오정훈 전국언론노동조합위원장, 전대식 지역신문노동조합협의회 의장(부산일보 지부장), 김명래 경인일보지부장, 민진영 경기민주언론시민연합 사무처장 등이 참여했다.

이들은 1인 시위를 통해 ‘네이버 뉴스 서비스 지역 언론 배제 개선’을 요구하고 ‘지역 공론장 형성을 위한 네이버의 공적 책임’을 촉구했다. 전국언론노조와 민언련은 매주 월요일마다 네이버 본사 앞 시위를 진행할 예정이다.

네이버는 최근 뉴스 서비스에 인공지능 에어스(AiRS) 알고리즘을 적용하는 방식으로 뉴스 편집 기능을 개편했다. 이후 지역 언론사 뉴스의 노출이 현격하게 줄어들었다. 아울러 100여 개 모바일 콘텐츠 제휴 언론사 중 독자가 구독을 선택할 수 있는 ‘채널’ 제휴사 44곳을 선정했는데 이 과정에서 지역 언론을 철저하게 배제했다. 이에 반발해 전국언론노조뿐 아니라 한국지방신문협회, 대한민국지방신문협의회 등 지역 신문 단체도 공동 성명을 발표하며 개선을 요구하고 나섰다. 전국시도의회의장협의회는 최근 총회에서 ‘네이버 지역 언론 배제 반대 성명’을 채택하기도 했다. 하지만 이 같은 반발에도 네이버는 뚜렷한 해결책을 내지 않고 있다.

오정훈 위원장은 1인 시위에서 “네이버는 해결책을 내놓기는커녕 뉴스제휴평가위원회에만 책임을 떠넘기고 있다”며 “지역 언론 배제 문제의 해결을 위한 대화 요구에 즉각 응답해 뉴스 유통사업자로서의 사회적 역할을 수행해야 한다”고 촉구했다.

전대식 의장은 “2005년 당시 네이버는 모든 언론사에 뉴스 유통망을 제공하는 우군이었지만 15년 만에 갑질하고 횡포하는 기업으로 전락했다”며 “지역 언론 종사자들이 만든 콘텐츠가 네이버에서 사라진 현실을 놓고 대화하고 상생적으로 풀어야 한다”면서 협의 창구 개설을 요구했다.

민언련은 국내 1위 포털 네이버가 지역 공론장을 만드는 사회적 책임을 외면하는 것은 현 정부의 지방분권 강화 정책에 위배되는 것이라고 지적했다.

민진영 사무처장은 “네이버가 지역신문에 대한 보도를 배제하고 시민들과의 소통 창구를 차단하는 것은 현 정부 정책인 지방분권 강화, 민주주의 정착이라는 큰 의제를 거역하는 것”이라며 “이런 행태는 반드시 중단돼야 하고 다양한 소식들이 소비자와 시민에게 전달돼야 한다”고 강조했다.

출처 : 제주新보(http://www.jejunews.com) 
'''
result = re.findall("네이버",str(text))
print(result)

numbers = """
010-2334-3234
02-302-3033
010-1321-4043
02-01-32
33-3303-3033
016-444-3042
"""

result2 = re.findall("\d{3}-\d{3,4}-\d{4}",numbers)
result3 = re.findall("0\d{1,2}-\d{3,4}-\d{4}",numbers)
print(result2)
print(result3)

email ="""
jkilee@gmail.com
kttredef@naver.com
akdef!aa.com
adekik@best.kr
abkereff@aacde
adefgree@korea.co.kr
"""
result4 = re.findall("\w+@\w+\.\w+\.?\w*",email)
print(result4)

text2 ="""
안녕하세요 저는 <em>홍길동</em> 입니다. 나이는 24살 세계 최고의 <a href="aa.aa.com">데이터 분석가</a>가 되고싶습니다.

"""
result5 = re.sub("<[^<]*>","",text2)
print(result5)

text3 ="""<p>
<span>네이버가 뉴스 서비스에 인공지능(AI)을 도입해 페이지 뷰(PV)를 늘리고 이용자를 끌어 모으고 있다.</span>
<span>네이버는 5일 오전 서울 강남구 그랜드 인터컨티넨털 호텔에서 AI 콜로키움 2019를 열고 이 같은 AI 성과와 전략을 소개했다.</span>
<span>이날 기조연설에서 김광현 네이버 서치앤클로바 리더는 "AI 뉴스 추천 시스템인 에어스(AiRS)를 도입하면서 뉴스 소비량이 확대되고 있다" 고 말했다.</span>
</p>"""
result6 = re.findall("<[^<]*>.*<[^<]*>",text3)
result7=[]
for i in range(len(result6)):
    result7.append(re.sub("<[^<]*>","",result6[i]))
print(result7)

rrmrm = re.findall(r'(?<=<span>).+(?=</span)',text3)
print(rrmrm)
import requests
from bs4 import BeautifulSoup

URL= 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
result = soup.select(".list_ranking tr > td.title a")
for i, v in enumerate(result):
    print(i+1, v.text)

URL= 'https://finance.naver.com/sise/sise_quant.nhn'
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
result = soup.select(".box_type_1 tr > td.title a")
for i, v in enumerate(result):
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
    print(i+1, v.text)