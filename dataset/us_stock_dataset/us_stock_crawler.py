"""
us stock crawler
"""

from dataset.base_crawler import BaseCrawler
import yfinance as yf
import pandas as pd
import os
from overrides import override

class USStockCrawler(BaseCrawler):
    
    def __init__(self):
        super().__init__()
        self.category = 'stock'
    
    @override
    def start_crawl(self, target, start, end, interval="1d"):
        """
        target: string, the name of the target, ex: "AAPL"
        start: string, the start date of data, ex: "2023-01-01"
        end: string, the end date of data, ex: "2023-01-02"
        interval: string, the frequency of the data, ex: "1d"
        """
        
        start_parse = ''.join(start.split('-'))
        end_parse = ''.join(end.split('-'))
        path = f'{self.data_store_path}/{self.category}-{target}-{start_parse}-{end_parse}'
        
        #check the cache
        if os.path.exists(path):
            self.logger.info(f'Data exist, load the data from {self.data_store_path}')
            data = pd.read_csv(path)
            return data

        #download the data
        data = yf.download(tickers=target, start=start, end=end, interval=interval)
        data.to_csv(path)
        return data