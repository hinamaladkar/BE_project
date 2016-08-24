from bs4 import BeautifulSoup
import requests
import csv
import xlrd

wb = xlrd.open_workbook(r'/home/aldel/students/it/113mihir4008/Desktop/mic/stocks_list.xlsx')
#b = wb.sheet_names()[0]
c = wb.sheet_by_name(wb.sheet_names()[0])
symbols = []
page = 0
for row in range(12, c.nrows):
    page += 1
    print(page)
    symbols.append(str(c.cell(row, 2).value))

    for symbol in symbols:
    	r = requests.get('https://www.google.com/finance/historical?q=NSE:' + symbol)
    	soup = BeautifulSoup(r.content, 'lxml')
    	with open('output.csv','a') as f:
        	a = f.write(symbol + ',' + soup.find_all('input', {'name': 'cid'})[0]["value"] + ',' + '\n')
    	#print(soup.find_all('input', {'name': 'cid'})[0]["value"])

	url = "https://www.google.com/finance/historical?cid="+soup.find_all('input', {'name': 'cid'})[0]["value"]+"&startdate=Jan+01%2C+2010&" \
		"enddate=Aug+18%2C+2016&num=30&ei=ilC1V6HlPIasuASP9Y7gAQ&start={}"



	with requests.session() as s:
	    start = 0
	    rows_list = []
	    req = s.get(url.format(start))
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
		
