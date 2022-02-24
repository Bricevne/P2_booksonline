import requests
from bs4 import BeautifulSoup
from functions.book_information import *


page_url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

response = requests.get(page_url)
response.encoding = 'utf8'

if response.ok:
    soup = BeautifulSoup(response.text, features="html.parser")
    number_of_article = int(soup.find("form", {"class" : "form-horizontal"}).find("strong").text)
    if number_of_article > 21:
        page_url = page_url.replace("index", "page-1")


response = requests.get(page_url)
response.encoding = 'utf8'

page_number = "1"

while response.ok:


    soup = BeautifulSoup(response.text, features="html.parser")

    books_page = soup.findAll("h3")
    for i in range(len(books_page)):
        books_page[i] = books_page[i].find("a")["href"].replace("../../..", "https://books.toscrape.com/catalogue")
        
    for books_nb in range(len(books_page)):
        response = requests.get(books_page[books_nb])
        response.encoding = 'utf8'

        if response.ok:
            soup = BeautifulSoup(response.text, features="html.parser")

            product_details = {}

            product_details["product_page_url"] = books_page[books_nb]
            product_table = soup.findAll("td")

            product_details["title"] = get_title(soup)
            product_details["universal_product_code"] = get_universal_product_code(product_table)
            product_details["price_including_tax"] = get_price_including_tax(product_table)
            product_details["price_excluding_tax"] = get_price_excluding_tax(product_table)
            product_details["number_available"] = get_number_available(product_table)
            product_details["product_description"] = get_product_description(soup)
            product_details["category"] = get_category(soup)
            product_details["review_rating"] = get_review_rating(soup)
            product_details["image_url"] = get_image_url(soup)

            print(product_details)

    if "page" in page_url:        
        next_page_number = int(page_number) + 1
        page_url = page_url.replace("page-" + str(page_number), "page-" + str(next_page_number))
        page_number = next_page_number
        
        response = requests.get(page_url)
        response.encoding = 'utf8'
    else:
        break


