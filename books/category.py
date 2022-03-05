"""
Categories control.
"""

def get_categories(soup_object: object) -> dict:
    categories = {}
    category_list = soup_object.find("ul", {"class" : "nav-list"}).find("li").findAll("li")
    for i in category_list:
        category_url = "https://books.toscrape.com/"  + i.find("a")["href"]
        category_name = i.find("a").text.replace(" ", "").replace("\n", "")
        categories[category_name] = category_url
    return categories