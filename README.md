# Webscraping Using Scrapy

In this project, the data is being scraped from https://www.worldometers.info/world-population/population-by-country/.   
This is probably the most simplest way of web scraping a website by creating spiders, using selectors like xpath, css-selectors.

### How To Install Scrapy
pip install scrapy
or
conda install -c conda-forge scrapy

### Creating Scrapy Project and Creating a Spider
scrapy startproject project_name

cd project_name
scrapy genspider spider_name www.example.com

### Executing Code
scrapy crawl spider_name

Note: must be at the same level as scrapy.cfg

### Notes
- Spider's see fetched website's without JavaScript.
- We should always return scraped data in a dictionary.