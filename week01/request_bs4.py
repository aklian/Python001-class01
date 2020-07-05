# 获取豆瓣前十电影信息
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://maoyan.com/films?showType=3'
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": 1,
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}
# reponse = requests.get(url, headers=header)
# html = reponse.text
with  open('/Users/v_lianqingwei/Downloads/maoyan.html', 'r') as f:
    html = f.read()
bs_info = bs(html, 'html.parser')
film_list = list()
for tags in bs_info.find_all('div', attrs={'class':'movie-hover-info'}):
    film_name = tags.find('span', attrs={'class':'name'}).text
    film_info = tags.find_all(class_='movie-hover-title')
    film_type = film_info[1].text.strip().split(" ")[-1]
    film_time = film_info[3].text.strip().split(" ")[-1]
    film_list.append({'name':film_name, 'type':film_type, 'online_time':film_time})


movie = pd.DataFrame(film_list)
movie.to_csv('./douban.csv', encoding='utf8', index=False, header=False)