import requests
import urllib.request
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# headers
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# urls
gold_url = "https://www.investing.com/commodities/gold-historical-data"
silver_url = "https://www.investing.com/commodities/silver-historical-data"

# returns a dictionary with the dates and prices in order from the given url
def get_prices(page):
    # page
    page = requests.get(page, headers=headers)
    # soup
    soup = BeautifulSoup(page.text, "html.parser")
    # table
    table = soup.find("table", {"id":"curr_table"})
    # body
    body = table.find("tbody")
    # rows
    rows = body.findAll("tr")

    # dict to return
    prices = []
    # populate dict
    for td in rows:
        row = td.text.split("\n")
        # convert date to iso format and store with price
        prices.append(( convert_date(row[1]), row[2] ))
    return prices

# takes a dictionary and a csvFile and stores the dictionary in the csv file
def store_dict(data, csv_file):
    try:
        with open(csv_file, "w") as db:
            writer = csv.writer(db)
            writer.writerow(["date","price"])
            # read each row in
            for row in data:
                writer.writerow(row)

    except IOError:
        print("I/O error: ", IOError)

# convert string date to iso format
def convert_date(date):
    date = date.replace(",", "")
    return datetime.strptime(date, "%b %d %Y")

# module
if __name__ == '__main__':
    # gold
    goldPrices = get_prices(gold_url)
    print(goldPrices)
    store_dict(goldPrices, "gold.csv")
    # silver
    silverPrices = get_prices(silver_url)
    print(silverPrices)
    store_dict(silverPrices, "silver.csv")