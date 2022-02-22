import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"

response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text, features="html.parser")


    product_information = soup.findAll("td")
    universal_product_code = product_information[0]
    title = soup.find("h1").text
    price_including_tax = product_information[3]
    price_excluding_tax = product_information[2]

    number_available_text = product_information[5].text
    number_available = "".join([character for character in number_available_text if character.isdigit()])
    print(number_available)
    product_description = soup.find("article", {"class" : "product_page"}).findAll("p")[3]
    category = soup.find("ul", {"class" : "breadcrumb"}).findAll("a")[2].text

    image_url = soup.find("img")["src"]
