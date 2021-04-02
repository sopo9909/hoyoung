import csv
from bs4 import BeautifulSoup
import bs4
#from BeautifulSoup import BeautifulSoup
reader =csv.reader(open('senior_lsf.csv','r'),delimiter=",")
svg = open('Seoul_districts.svg','r').read()
min_value = 100;max_value = 0; past_header = False
senior_count={}
counts_only=[]
for row in reader:
    if not past_header:
        past_header = True
        continue
    try:
        unique =row[0]
        count=float(row[1].strip())
        senior_count[unique]=count
        counts_only.appendp(count)
    except:
        pass
soup = BeautifulSoup(svg, 'html.parser')
paths = soup.findAll('path')
colors = ["#FFE7D3","#FFA47C",'#FF805C','#DB291B',"#B71314","#7A071A"]
path_style = 'font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'
for p in paths:
    if p['id']:
        try:
            count = senior_count[p['id']]
        except:
            continue
        if count > 500000:
            color_class = 5
        elif count > 400000:
            color_class = 4
        elif count > 300000:
            color_class = 3
        elif count > 200000:
            color_class = 2
        elif count > 100000:
            color_class = 1
        else:
            color_class = 0
        color = colors[color_class]
        p['style'] = path_style + color
print(soup.prettify())