# webtoon_rate_scraping_one_page.py
from bs4 import BeautifulSoup
import requests
import pandas as pd #as alias

url = 'https://comic.naver.com/webtoon/list'
params = {
    'titleId' : '746834',
    'page': '1'
}
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
}
res = requests.get(url,params=params, headers=headers)
#print(res)
#print(res.text)

#파싱 (구문 분석, 단순 문자열로 써져있는 HTML을 구조 분석하는 것)
html = BeautifulSoup(res.text, 'lxml')


#찾아야될 정보- 점수, 회차별제목
titles = html.select('.title > a')
rates = html.select('.rating_type > strong')

titles = [t.text for t in titles]
rates = [float(r.text) for r in rates]
print(titles, rates)


# 엑셀로 저장하기
data = [rates] # 이중 리스트
col = titles
data_frame = pd.DataFrame(data, columns=col)
data_frame.to_excel('청춘블라썸.xlsx', sheet_name='샘플', startrow=0, header=True)