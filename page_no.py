import requests
import re
from bs4 import BeautifulSoup
r = requests.get('https://www.google.com/finance/historical?cid=13564339&startdate=Jan+01%2C+2010&enddate=Aug+18%2C+2016&num=30&ei=ilC1V6HlPIasuASP9Y7gAQ')
soup = BeautifulSoup(r.content,'lxml')
var = soup.find_all("script")[8].string
a = re.compile('google.finance.applyPagination\((.*)\'http', re.DOTALL)
b =  a.search(var)
num = b.group(1)
print(num.replace(',','').split('\n')[3])