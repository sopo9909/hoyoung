<<<<<<< HEAD
import json
import requests
from bs4 import BeautifulSoup
response=requests.get("https://scrapying-study.firebaseapp.com/05/")
result_dic=json.loads(response.text)
print(result_dic)
with open("data.json","w") as json_file:
=======
import json
import requests
from bs4 import BeautifulSoup
response=requests.get("https://scrapying-study.firebaseapp.com/05/")
result_dic=json.loads(response.text)
print(result_dic)
with open("data.json","w") as json_file:
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
    json.dump(result_dic,json_file)