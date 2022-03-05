"""
Books' pages control.
"""

import requests
from bs4 import BeautifulSoup



def format_page_url(url: str) -> str:
    response = requests.get(url)
    response.encoding = 'utf8'
    if response.ok:
        soup = BeautifulSoup(response.text, features="html.parser")
        number_of_article = int(soup.find("form", {"class" : "form-horizontal"}).find("strong").text)
        if number_of_article > 20:
            return url.replace("index", "page-1")
    return url


def get_next_page(page_number: int, url: str) -> list:
    next_page_number = page_number + 1
    url = url.replace("page-" + str(page_number), "page-" + str(next_page_number))
    page_number = next_page_number
    return url
