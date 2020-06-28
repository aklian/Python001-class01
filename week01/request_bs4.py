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
    "Cookie": "uuid_n_v=v1; uuid=231642B0B93811EA96060F060440817E5E58AD9A47644B7492C19A913E694AEC; _csrf=0e5ecc3597a313d4c907f3d01f188cb67f7f3efbe245b223dd3757c0aa4a1551; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593346136; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593346136; _lxsdk_cuid=172fad49873c8-059cae7a439f1a-31617402-fa000-172fad49874c8; _lxsdk=231642B0B93811EA96060F060440817E5E58AD9A47644B7492C19A913E694AEC; __mta=214867240.1593346136646.1593346136646.1593346136646.1; mojo-uuid=92d10e17d9e326537b4a9820ec150fd2; mojo-session-id={\"id\":\"5429e2e3f4b18114bd2950acd13d49fe\",\"time\":1593346137147}; mojo-trace-id=1; _lxsdk_s=172fad49875-b31-2a-667%7C%7C2",
    "DNT":1,
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": 1,
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}
reponse = requests.get(url, headers=header)
html = reponse.text
# with  open('/Users/v_lianqingwei/Downloads/maoyan.html', 'r') as f:
#    html = f.read()
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