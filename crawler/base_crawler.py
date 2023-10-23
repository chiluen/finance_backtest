"""
Crawler interface
"""

class BaseCrawler():
    
    def __init__(self):
        self.data_store_path = './data_storage'
    
    def set_environment(self):
        """Set the basic setting for different crawler"""
        pass
    
    def start_crawl(self):
        """Start to run the crawl"""
        pass
        