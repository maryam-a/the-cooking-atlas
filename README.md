# The Cooking Atlas

This project was created in an attempt to learn more about the different
cuisines and cultures around the world.

## Getting Started

Feel free to skip to the [other section](#choosing-a-popular-dish-from-a-random-country)
if you want to use the list of countries and dishes that I've compiled.

### Requirements

- Python 3 (If you don't have this already, download the Anaconda distribution)
- Install the following dependencies:

```bash
pip install requests
pip install urllib
pip install beautifulsoup4
pip install webbrowser
```

### Generating the list of countries and dishes

Originally, I wanted to scrape [Wikipedia's National Dish page](https://en.wikipedia.org/wiki/National_dish)
to compile a list of all of the countries in the world and their popular dishes.
Due to the HTML structure of the page, it proved too time consuming to figure
out how which selectors would be ideal to get all of the country and dish
information. (Feel free to make a PR if you'd like to help with this 😊).

Instead, I scraped a web page with all the countries and then manually added
the dishes.

1. Open `national-dish.py`.
2. Uncomment the call to `fetch_countries()` in the `__main__` code block and 
comment out the others.
3. Run the file.
4. For each country, add the dish names. If more than one, they must be comma
separated. Each line must end with a comma.

### Choosing a popular dish from a random country

1. Open `national-dish.py`.
2. Ensure that the last two method calls in the `__main__` code block are 
uncommented and the previous method call commented.
3. Run the file.
4. Two new tabs should have opened in your default browser - one with a search
for the country and another for the selected recipe.
5. Have fun learning about the history and culture of the country and enjoy
your meal!

## Contributing

If you would like contribute to this project, please make a PR - especially if you'd like to add dishes to my current list :)
