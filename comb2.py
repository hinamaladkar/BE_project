from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

symbols = []
cid = []
sym = []
page = 0

df = pd.read_csv(r'C:\Users\Vaishu_2\Desktop\output1.csv', names = ['symbols','cid'])
for s in df.symbols:
	symbols.append(s)

for c in df.cid:
	cid.append(c)

for i in range(0,25):
	sym.append[i]
	

print(symbols)
for symbol in symbols:
    print(symbol)
    print("hii")

    url = "https://www.google.com/finance/historical?cid="+str(int(cid[page]))+"&startdate=Jan+01%2C+2010&" \
	    "enddate=Aug+18%2C+2016&num=30&ei=ilC1V6HlPIasuASP9Y7gAQ&start={}"
    print(str(int(cid[page])))
    page+=1

    with requests.session() as s:
        start = 0
        rows_list = []
        req = s.get(url.format(start))
        print(url.format(start))
        soup = BeautifulSoup(req.content, "lxml")
        table = soup.select_one("table.gf-table.historical_price")
        all_rows = table.find_all("tr")
        while True:
            soup = BeautifulSoup(s.get(url.format(start)).content, "lxml")
            table = soup.select_one("table.gf-table.historical_price")
            if not table:
                break
            all_rows.extend(table.find_all("tr"))
            #print(all_rows)
            for row in table.find_all("tr"):
                row_list = []
                cells = row.find_all("td")
                #print(len(cells))
                try:
                    row_list.extend([str(cells[0].text.replace('\n','')), str(cells[1].text.replace('\n','')), str(cells	[2].text.replace('\n','')), str(cells[3].text.replace('\n','')), str(cells[4].text.replace('\n','')), str(cells[5].text.replace('\n',''))])
                except:
                    pass
                rows_list.append(row_list)
                #print(rows_list)
                with open(symbol+".csv",'w') as fu:
                    data = csv.writer(fu)
                    for row in rows_list:
                        data.writerow(row)
            start += 30
            #print(start)
