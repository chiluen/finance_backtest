"""
Model interface
"""

from utils.logger import get_logger
import yaml

class BaseModel():
    
    def __init__(self, customized_parameters=None):
        """Init, customized_parameters should be in the dictionary format"""
        self.model = None
        self.config = None
        self.logger = get_logger(__name__)
    
    def _set_config(self, config_path):
        """Prepare for the overall config"""
        with open(config_path, 'r') as f:
            self.config = yaml.full_load(f)
        
    def _set_model_config(self, customized_parameters):
        """Set the config for model and override for the customized_parameters"""
        model_config = self.config['parameters']
        if customized_parameters is not None:
            for key, value in customized_parameters.items():
                if key not in model_config:
                    self.logger.error(f'Customized parameter could not be loaded, please check for the valid option in {config_path}')
                    raise RuntimeError()
                model_config[key] = value
        return model_config
    
    def _set_model(self, model_config):
        """Set the model by DIP"""
        pass
    
    def train(self, data, target):
        """Train for the self.model"""
        pass
        
    def evaluate(self, data):
        """Evaluate for the data"""
        pass