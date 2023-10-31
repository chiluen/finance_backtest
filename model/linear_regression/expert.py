"""
Linear regression model
"""

from model.base_model import BaseModel
from overrides import override
from sklearn.linear_model import LinearRegression

class LinearRegressionModel(BaseModel):
    
    def __init__(self, customized_parameters=None):
        super().__init__()
        
        #set the config
        config_path = './model/linear_regression/config.yaml'
        self._set_config(config_path)
        
        #set the model
        model_config = self._set_model_config(customized_parameters)
        self._set_model(model_config)
    
    @override
    def _set_model(self, model_config):
        self.model = LinearRegression(**model_config)
    
    @override
    def train(self, data, target):
        self.model.fit(data,target)
    
    @override
    def evaluate(self, data):
        predict = self.model.predict(data)
        
        return predict
        
        
        
    
        