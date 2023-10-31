"""
us stock dataset
"""

from dataset.base_dataset import BaseDataset
from dataset.us_stock_dataset.us_stock_crawler import USStockCrawler
from overrides import override


class USStockDataset(BaseDataset):
    
    def __init__(self):
        super().__init__()
        self._init_environment()
        
    @override
    def _init_environment(self):
        self._crawler = USStockCrawler()
        
    @override
    def prepare_data(self, target, start, end, interval="1d"):
        self._data = self._crawler.start_crawl(target, start, end, interval)
        self._set_target()
        
    @override
    def _set_target(self):
        self._data['target'] = self._data['Close']
        
    @override
    def train_test_split(self, window_size=3):
        if self._data is None:
            self.logger.error('Plase call the prepare_data() first')
            raise RuntimeError()
            
        train_start_index = 0
        test_start_index = train_start_index+window_size+1
        
        while(test_start_index < len(self._data)):
            temp_train_split_index = (train_start_index, train_start_index+window_size)
            self._train_split_index.append(temp_train_split_index)
            self._test_split_index.append(test_start_index)
            train_start_index += 1
            test_start_index += 1

        self.logger.info(f'Window size is {window_size}')
        self.logger.info(f'Complete the train and test split, the length of them is {len(self._train_split_index)}')
    
    @override
    def get_train_split(self, index):
        return self._data.iloc[self._train_split_index[index][0]:self._train_split_index[index][1],:]
    
    @override
    def get_test_split(self, index):
        return self._data.iloc[[self._test_split_index[index]],:] 