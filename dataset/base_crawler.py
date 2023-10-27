"""
Crawler interface
"""

from utils.logger import get_logger

class BaseCrawler():
    
    def __init__(self):
        self.data_store_path = './data_storage'
        self.logger = get_logger(__name__)
    
    def set_environment(self):
        """Set the basic setting for different crawler"""
        pass
    
    def start_crawl(self, target, start, end, interval):
        """Start to run the crawl"""
        pass
        