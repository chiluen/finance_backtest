"""
Dataset interface
"""

from utils.logger import get_logger

class BaseDataset():
    
    def __init__(self):
        """
        self._data: pandas.DataFrame
        self._train_split_index: the index to get the data 
        """
        self._data = None
        self._train_split_index = []
        self._test_split_index = []
        
        self._crawler = None
        self.logger = get_logger(__name__)
    
    def _init_environment(self):
        """Set the environment"""
        pass
        
    def prepare_data(self, target, start, end, interval):
        """Get the data, and prepare data in df format"""
        pass
    
    def train_test_split(self, window_size):
        """Split the train test data"""
        pass
    
    def get_train_split(self, index):
        """Get trin split by index"""
        pass
    
    def get_test_split(self, index):
        """Get test split by index"""
        pass
    
    def get_train_test_length(self):
        """Get the train/test split len"""
        return len(self._train_split_index)
