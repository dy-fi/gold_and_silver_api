from flask import Flask
from flask import request
from flask import jsonify

import csv
from datetime import date, datetime, timedelta
import dateutil.parser as parser
import numpy as np

app = Flask(__name__)

# returns datetime objects in a range between the start and end date
def get_date_range(start, end):
    # convert start to iso
    start = parser.parse(start)
    end = parser.parse(end)
    # get ran
    dates = [str(start + timedelta(days=x)) for x in range(0, (end-start).days + 1)]
    return dates

# return a dictionary of matching prices from csv database given the dates
def get_pairs(dates, csv_file):
    result = {}
    with open(csv_file, "r") as db:
        reader = csv.reader(db)
        for row in reader:
            if row[0][:10] in str(dates):
                result[row[0][:10]] = row[1].replace(",", "")
    
    return result


@app.route('/commodity')
def index():
    # queries
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    commodity_type = request.args.get("commodity_type")
    
    # get date range
    dates = get_date_range(start_date, end_date)
    # get date,price pair for that range
    pairs = get_pairs(dates, commodity_type + ".csv")

    # get mean, variance
    prices = np.array(list(pairs.values())).astype(float)
    mean = np.mean(prices)
    variance = np.var(prices)

    return jsonify(data=pairs, mean=mean, variance=variance)
    
# module
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=True)