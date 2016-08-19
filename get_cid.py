#inti
import requests
import xlrd
from bs4 import BeautifulSoup

wb = xlrd.open_workbook(r'C:\Users\Jeri_Dabba\Desktop\stocks_list.xlsx')
#b = wb.sheet_names()[0]
c = wb.sheet_by_name(wb.sheet_names()[0])
symbols = []

for row in range(12, c.nrows):
    symbols.append(str(c.cell(row, 2).value))

for symbol in symbols:
    r = requests.get('https://www.google.com/finance/historical?cid='+symbol+'&startdate=Jan+01%2C+2010&enddate=Aug+18%2C+2016&num=30&ei=ilC1V6HlPIasuASP9Y7gAQ')
    soup = BeautifulSoup(r.content, 'lxml')
    with open('output.txt','a') as f:
        f.write(symbol + ',' + soup.find_all('input', {'name': 'cid'})[0]["value"] + ',' + '\n')
    print(soup.find_all('input', {'name': 'cid'})[0]["value"])
    var = soup.find_all("script")[8].string
    a = re.compile('google.finance.applyPagination\((.*)\'http', re.DOTALL)
    b =  a.search(var)
    num = b.group(1)
    print(num.replace(',','').split('\n')[3])