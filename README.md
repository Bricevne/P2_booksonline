# Utilisez les bases de Python pour l'analyse de marché - Openclassrooms project 2

This project offers a program capable of scraping through the different categories of novels in order to exctract books' information from an online library. it will return csv files for each book category summing up all books details within this category, as well as save all books' images.

The website to scrape can be seen at this address : https://books.toscrape.com/

## Installation
Clone the repository on your computer.

Set your virtual environment under python 3.10

pipenv install  # create the virtual environment and install the dependencies
pipenv shell  # activate the virtual environment

pipenv install -r requirements.txt # install the necessary libraries in the virtual environnement


## Usage

python main.py  # run the code to scrape the website and obtain all books information with csv

## License
MIT