from bs4 import BeautifulSoup
import requests

url = "https://www.google.com/finance/historical?cid=13564339&startdate=Jan+01%2C+2015&" \
      "enddate=Aug+18%2C+2016&num=30&ei=ilC1V6HlPIasuASP9Y7gAQ&start={}"

#url = 'https://www.google.com/finance/historical?cid=13564339&startdate=Aug+21%2C+2014&enddate=Aug+19%2C+2016&num=30&ei=Zva2V6mlC8WsugSomoS4Ag'


with requests.session() as s:
    start = 0
    req = s.get(url.format(start))
    soup = BeautifulSoup(req.content, "lxml")
    table = soup.select_one("table.gf-table.historical_price")
    all_rows = table.find_all("tr")
    while True:
        start += 30
        soup = BeautifulSoup(s.get(url.format(start)).content, "lxml")
        table = soup.select_one("table.gf-table.historical_price")
        if not table:
            break
        all_rows.extend(table.find_all("tr"))
