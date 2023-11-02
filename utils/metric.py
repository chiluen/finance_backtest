"""
Metric for the evaluation
"""

from sklearn.metrics import mean_squared_error

def mean_square_error(prediction_list, ans_list):
    return mean_squared_error(prediction_list, ans_list)