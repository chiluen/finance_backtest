"""
pipeline interface
"""

from utils.logger import get_logger

class BasePipeline():
    
    def __init__(self, dataset, model):
        self.dataset = dataset
        self.model = model
        self.logger = get_logger(__name__)
        
    def run(self):
        """run train and test, show the result"""
        pass
    
    def prepare_data(self, index):
        """Get the dataset by index"""
        pass
    
