"""
pipeline interface
"""

from utils.logger import get_logger

class BasePipeline():
    
    def __init__(self, dataset, model):
        self.dataset = dataset
        self.model = model
        self.logger = get_logger(__name__)
        
    def _set_model_dataset(self):
        """set for the dataset and model"""
        
    def run(self):
        """run train and test, show the result"""
        pass
    
    def plot(self):
        """plot for the outcome"""
        pass