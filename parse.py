from bs4 import BeautifulSoup as bs
import json


def parse_html(html_content) -> str:
    soup = bs(html_content, 'lxml')
    l = soup.find('ul', attrs={'id': "thread_list"})
    li = l.find('li', attrs={'class': "j_thread_list clearfix thread_item_box"})
    article_href = li.find('a', attrs={'class': "j_th_tit"}).get('href')

    return article_href


def parse_cache(file_name) -> str:
    with open(file_name, 'r', encoding='utf-8') as f:
        c = f.read()
        if c:
            return parse_html(c)
        else:
            return ""


def parse_article(article_content) -> dir:
    soup = bs(article_content, 'lxml')
    tit = soup.find('h3').get('title')
    top_floor = soup.find('div', attrs={'class': 'd_post_content j_d_post_content'})
    text = top_floor.text
    img = [img.get('src') for img in top_floor.find_all('img')]

    js = {'post_type': 'mp', 'title': tit}
    if text:
        js['text'] = text.strip()
    if img:
        js['img'] = img

    return js
