import requests
from urllib.parse import urljoin
import parse
import args


def html_update(url_tup: tuple, use_cache=False, update_cache=False):
    if use_cache:
        article_href = urljoin(url_tup[0], parse.parse_cache("html_content.html"))
    else:
        file_name = None
        if update_cache:
            file_name = "html_content.html"
        html_content = request(urljoin(url_tup[0], url_tup[1]), file_name)
        article_href = urljoin(url_tup[0], parse.parse_html(html_content))

    if use_cache:
        f = open("html_article.html", "r", encoding='utf-8')
        article_text = f.read()
    else:
        article_text = request(article_href)
    js = parse.parse_article(article_text)

    return js


def request(url, file_name=None):
    response = requests.get(url)
    if response.status_code == 200:
        text = response.text
        if file_name:
            with open(file_name, 'w', encoding=response.encoding, newline='') as f:
                f.write(text)
        return text
    else:
        raise "fail"


if __name__ == '__main__':
    arguments = args.get_args()
    print(html_update((arguments.head, arguments.url), use_cache=True))
