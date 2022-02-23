import requests
from bs4 import BeautifulSoup
from urllib import request


url = "http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"

response = requests.get(url)
response.encoding = 'utf8'

if response.ok:
    soup = BeautifulSoup(response.text, features="html.parser")

    product_details = {}
    current_url=request.Request(url)
    product_details["product_page_url"] = current_url.get_full_url()
    product_details["title"] = soup.find("h1").text

    product_table = soup.findAll("td")
    product_details["universal_product_code"] = product_table[0].text
    title = soup.find("div", {"class" : "product_main"}).text
    product_details["price_including_tax"] = product_table[3].text
    product_details["price_excluding_tax"] = product_table[2].text

    number_available_text = product_table[5].text
    product_details["number_available"] = "".join([character for character in number_available_text if character.isdigit()])
    
    product_details["product_description"] = soup.find("article", {"class" : "product_page"}).findAll("p")[3].text
        
    product_details["category"] = soup.find("ul", {"class" : "breadcrumb"}).findAll("a")[2].text

    product_details["review_rating"] = soup.find("p", {"class" : "star-rating"})["class"][1]

    image_url = soup.find("img")["src"]
    product_details["image_url"] = image_url.replace("../..", "https://books.toscrape.com/")

    print(product_details)
