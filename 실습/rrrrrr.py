from bs4 import BeautifulSoup
import requests
url="https://www.basenotes.net/fragrancedirectory/?launch1=2020&launch=1&p=1"
response = requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
result = soup.find_all(attrs={'valign':'top'})
for i in result:
    url=i.find('a')["href"]
    response = requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, "html.parser")
    product_name=soup.find(attrs={'itemprop':'name'})
    brand_name=soup.find(attrs={'itemprop':'brand manufacturer'})
    print('product_name : ',product_name.text,'brand_name : ',brand_name.text)
    try:
        rate=soup.find(attrs={'itemprop':'ratingValue'})["content"]
        print('rating : '+rate)
    except:
        pass
    try:
        review=soup.find(attrs={'class':'reviewblurb'})
        print('리뷰 :'+review.text.replace('\n',''))
    except:
        pass
    try:
        note=soup.find(attrs={'class':'notespyramid notespyramidb'})
        print(note.text.replace('\n',''))
    except:
        pass