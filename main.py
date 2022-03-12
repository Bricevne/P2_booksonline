"""Main entry point of the application."""


import shutil
from os import path

import requests
from bs4 import BeautifulSoup

from books.book_information import (
    get_category,
    get_image_url,
    get_number_available,
    get_price_excluding_tax,
    get_price_including_tax,
    get_product_description,
    get_review_rating,
    get_title,
    get_universal_product_code,
)
from books.category import get_categories
from books.page import format_page_url, get_next_page
from output_control.folder_control import create_output_folders

CSV_HEADER = [
    "product_page_url",
    "universal_product_code",
    "title",
    "price_including_tax",
    "price_excluding_tax",
    "number_available",
    "product_description",
    "category",
    "review_rating",
    "image_url",
]


page_url = "https://books.toscrape.com/index.html"

response = requests.get(page_url)
response.encoding = "utf8"

categories = {}
if response.ok:
    soup = BeautifulSoup(response.text, features="html.parser")
    categories = get_categories(soup)

output_path = "products"
create_output_folders(output_path, categories)

books_counter = 0
for category, url in categories.items():
    with open(f"products/information/{category}.csv", "w") as file:
        first_line = ""
        for headers in CSV_HEADER:
            first_line += headers
            if headers != CSV_HEADER[-1]:
                first_line += ";"
        first_line += "\n"
        file.write(first_line)

    page_url = format_page_url(url)

    response = requests.get(page_url)
    response.encoding = "utf8"

    page_number = 1
    while response.ok:

        soup = BeautifulSoup(response.text, features="html.parser")
        books_page = soup.findAll("h3")

        for i in range(len(books_page)):
            books_page[i] = (
                books_page[i]
                .find("a")["href"]
                .replace("../../..", "https://books.toscrape.com/catalogue")
            )

        for book_url in range(len(books_page)):
            response = requests.get(books_page[book_url])
            response.encoding = "utf8"

            if response.ok:

                product_details = {}
                soup = BeautifulSoup(response.text, features="html.parser")

                product_details["product_page_url"] = books_page[book_url]
                product_table = soup.findAll("td")
                product_details["universal_product_code"] = get_universal_product_code(
                    product_table
                )
                product_details["title"] = get_title(soup)
                product_details["price_including_tax"] = get_price_including_tax(
                    product_table
                )
                product_details["price_excluding_tax"] = get_price_excluding_tax(
                    product_table
                )
                product_details["number_available"] = get_number_available(
                    product_table
                )
                product_details["product_description"] = get_product_description(soup)
                product_details["category"] = get_category(soup)
                product_details["review_rating"] = get_review_rating(soup)
                product_details["image_url"] = get_image_url(soup)

                image_title = (
                    product_details["title"].replace(" ", "-").replace("/", "-")
                )
                file = f"products/images/{category}/{image_title}.jpg"

                if path.exists(file):
                    image_title += "(bis)"

                response = requests.get(product_details["image_url"], stream=True)
                if response.ok:
                    with open(
                        f"products/images/{category}/{image_title}.jpg", "wb"
                    ) as file:
                        response.raw.decode_content = True
                        shutil.copyfileobj(response.raw, file)

                with open(f"products/information/{category}.csv", "a") as file:
                    line = ""
                    for headers in CSV_HEADER:
                        line += product_details[headers]
                        if headers != CSV_HEADER[-1]:
                            line += ";"
                    line += "\n"
                    file.write(line)

                books_counter += 1
                print(f"Book n°{books_counter}")

        if "page" in page_url:
            page_url = get_next_page(page_number, page_url)
            page_number += 1
            response = requests.get(page_url)
            response.encoding = "utf8"
        else:
            break
