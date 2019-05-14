import data
import unittest
from datetime import datetime

# urls
gold_url = "https://www.investing.com/commodities/gold-historical-data"
silver_url = "https://www.investing.com/commodities/silver-historical-data"

gold_prices = data.get_prices(gold_url)
silver_prices = data.get_prices(silver_url)


class DataTest(unittest.TestCase):
    
    def test_get_prices_gold(self):
        assert gold_prices is not None
        assert len(gold_prices) > 25

    def test_get_prices_silver(self):
        assert silver_prices is not None
        assert len(silver_prices) > 25

    def test_store_dict(self):
        assert data.store_dict(gold_prices, "gold.csv") is not IOError
        assert data.store_dict(silver_prices, "silver.csv") is not IOError

    def test_convert_date(self):
        assert data.convert_date("Apr 14, 2019") == datetime(2019, 4, 14, 0, 0) # with comma
        assert data.convert_date("May 14, 2019") == datetime(2019, 5, 14, 0, 0) # without comma

if __name__ == '__main__':
    unittest.main()
