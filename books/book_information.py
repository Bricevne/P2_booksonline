"""Functions to get all the book's information."""


def get_title(soup_object: object) -> str:
    """Return book title."""
    return soup_object.find("h1").text


def get_universal_product_code(product_information_table: list) -> str:
    """Return book UPC."""
    return product_information_table[0].text


def get_price_including_tax(product_information_table: list) -> str:
    """Return book price including tax."""
    return product_information_table[3].text


def get_price_excluding_tax(product_information_table: list) -> str:
    """Return book price excluding tax."""
    return product_information_table[2].text


def get_number_available(product_information_table: list) -> str:
    """Return number of books available."""
    number = product_information_table[5].text
    return "".join([character for character in number if character.isdigit()])


def get_product_description(soup_object: object) -> str:
    """Return book description."""
    if soup_object.find("div", {"id": "product_description"}) != None:
        description = (
            soup_object.find("article", {"class": "product_page"}).findAll("p")[3].text
        )
    else:
        description = "No description yet."
    return description.replace(";", ",")


def get_category(soup_object: object) -> str:
    """Return book category."""
    return soup_object.find("ul", {"class": "breadcrumb"}).findAll("a")[2].text


def get_review_rating(soup_object: object) -> str:
    """Return book review rating."""
    return soup_object.find("p", {"class": "star-rating"})["class"][1]


def get_image_url(soup_object: object) -> str:
    """Return book image url."""
    image_url = soup_object.find("img")["src"]
    return image_url.replace("../..", "https://books.toscrape.com/")
