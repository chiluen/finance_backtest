"""
us stock crawler
"""

from crawler.base_crawler import BaseCrawler
import yfinance as yf
import pandas as pd
import os

class USStockCrawler(BaseCrawler):
    
    def start_crawl(self, stock, start, end, interval="1d"):
        
        start_parse = ''.join(start.split('-'))
        end_parse = ''.join(end.split('-'))
        path = f'{self.data_store_path}/{stock}-{start_parse}-{end_parse}'
        
        #check the cache
        if os.path.exists(path):
            print('data exist') # should be replace by logger
            data = pd.read_csv(path)
            return data

        #download the data
        data = yf.download(tickers=stock, start=start, end=end, interval=interval)
        data.to_csv(path)
        return data