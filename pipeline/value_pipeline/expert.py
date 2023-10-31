"""
Pipeline for value prediction
"""

from pipeline.base_pipeline import BasePipeline
from overrides import override
from sklearn.metrics import mean_squared_error

class ValuePipeline(BasePipeline):
    
    def __init__(self, dataset, model):
        super().__init__(dataset, model)
        
    @override
    def run(self):
        #TODO: Need to think how to adapt the model to all circumstance(adding another protocal?)
        
        #valid model and dataset
        if self.dataset.get_train_test_length() == 0:
            self.logger.error('You should specify data of dataset by dataset.prepare_data and dataset.train_test_split() first!')
            raise RuntimeError
        
        value_list = []
        ans_list = []
        
        #todo: 是不是要加上一個進度條？
        for i in range(self.dataset.get_train_test_length()):
            #是不是把data弄成 train_data永遠都是從index=0到index=現在？
            #todo: 還需要針對資料做清理，要寫成額外一個function（）
            # train_data = self.dataset.get_train_split(i)
            # train_data_X = train_data.drop('target', axis=1)
            # train_data_Y = train_data['target']
            # test_data = self.dataset.get_test_split(i)
            # test_data_X = test_data.drop('target', axis=1)
            # test_data_Y = test_data['target']
            train_data_X, train_data_Y, test_data_X, test_data_Y = self.prepare_data(i)
            
            self.model.train(train_data_X, train_data_Y)
            result = self.model.evaluate(test_data_X)
            value_list.append(result)
            ans_list.append(test_data_Y)
        #還需要一個evaluate function，現在先用一個MSE好了
        print(mean_squared_error(value_list, ans_list))
    
    def prepare_data(self, index):
        """return and postprocess data"""
        train_data = self.dataset.get_train_split(index)
        train_data = train_data.loc[:, (train_data.dtypes == 'float64') | (train_data.dtypes == 'int64')] #filter out the non-numeric data
        train_data_X = train_data.drop('target', axis=1)
        train_data_Y = train_data['target']
        
        test_data = self.dataset.get_test_split(index)
        test_data = test_data.loc[:, (test_data.dtypes == 'float64') | (test_data.dtypes == 'int64')] #filter out the non-numeric data
        test_data_X = test_data.drop('target', axis=1)
        test_data_Y = test_data['target']
        return train_data_X, train_data_Y, test_data_X, test_data_Y
            
            
        
        
    