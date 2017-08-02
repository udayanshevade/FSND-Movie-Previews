# Movie Preview Website

## Live site
The compiled page can be found [here](http://udayanshevade.github.io/FSND-Movie-Previews)

## Description
Compiles a server-rendered page with python, utilizing data fetched from the TMDB API. Jinja2 is used for templating and the client side uses Materialize CSS and jQuery.

## Installation
1. Download or clone the [project repo](https://github.com/udayanshevade/FSND-Movie-Previews)
2. `pip install -r requirements.txt` for any required packages
 - If you need `pip`, get it [here](https://packaging.python.org/tutorials/installing-packages/#install-pip-setuptools-and-wheel)
3. Replace the placeholder for <<YOUR_API_KEY>> in `entertainment_center.py` with your API key (directions below)
4. Build `entertainment_center.py`
5. Click on a card to focus on the details of a movie. Click the play button to see its trailer.

### Getting an TMDB key
1. Create a TMDB account and follow the directions [here](https://www.themoviedb.org/faq/api)