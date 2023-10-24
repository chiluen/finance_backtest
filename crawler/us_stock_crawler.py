"""
us stock crawler
"""

from crawler.base_crawler import BaseCrawler
import yfinance as yf
import pandas as pd
import os
from utils.logger import get_logger

class USStockCrawler(BaseCrawler):
    
    def __init__(self):
        super().__init__()
        self.logger = get_logger(__name__)
    
    def start_crawl(self, stock, start, end, interval="1d"):
        
        start_parse = ''.join(start.split('-'))
        end_parse = ''.join(end.split('-'))
        path = f'{self.data_store_path}/{stock}-{start_parse}-{end_parse}'
        
        #check the cache
        if os.path.exists(path):
            self.logger.info("Data exist")
            data = pd.read_csv(path)
            return data

        #download the data
        data = yf.download(tickers=stock, start=start, end=end, interval=interval)
        data.to_csv(path)
        return data