# -*- coding: utf-8 -*-
"""
@author: maryam-a
"""

import requests
from bs4 import BeautifulSoup
import random
from urllib.request import urlretrieve
from urllib.parse import quote
import webbrowser

# Constants: Edit if necessary
COUNTRY_LIST = "https://www.britannica.com/topic/list-of-countries-1993160"
COUNTRY_SELECTORS = "ul li div a"
FILE_NAME = "./national-dish.txt"
SEARCH_URL = "https://www.bing.com/search?q={}"  # bing
# SEARCH_URL ="https://www.google.com/search?q={}" # google


def fetch_countries():
    """
    Scrapes a website to get the list of countries and writes it to a file.
    """

    doc = open(FILE_NAME, "w")

    page = requests.get(COUNTRY_LIST)
    soup = BeautifulSoup(page.content, 'html.parser')

    country_links = soup.select(COUNTRY_SELECTORS)

    for country in country_links:
        doc.write(country.get_text() + ' | \n')

    doc.close()


def choose_country_and_dish():
    """
    Randomly selects a country and a dish to make.

    Returns:
        (str, str) - the randomly selected country, the randomly selected dish
    """
    line = random.choice(open(FILE_NAME, encoding="utf8").readlines())
    line_split = line.split("|")
    country = line_split[0].strip()
    dishes = []
    for dish in line_split[1].split(","):
        potential_dish = dish.strip()
        if len(potential_dish) != 0:
            dishes.append(potential_dish)

    final_dish = random.choice(dishes)
    print(f"This week's dish is {final_dish} from {country}!")

    return country, final_dish


def perform_searches(country, dish_name):
    """
    Opens new tabs in the user's default browser with searches of the country
    and the chosen recipe for that country.

    Args:
        country (str) - the country of interest
        dish_name (str) - the name of the dish from the country of interest
    """
    if not country or not dish_name:
        raise ValueError("The country or dish name was not provided.")

    country_url = SEARCH_URL.format(quote(country))
    webbrowser.open_new_tab(country_url)

    recipe_url = SEARCH_URL.format(
        quote(country + " " + dish_name + " recipe"))
    webbrowser.open_new_tab(recipe_url)


if __name__ == '__main__':
    ## Uncomment the line below to generate the country list + comment out 
    ## the other two method calls.
    ## Otherwise, comment the line below + uncomment the other two method calls.
    # fetch_countries()

    country, dish = choose_country_and_dish()
    perform_searches(country, dish)
