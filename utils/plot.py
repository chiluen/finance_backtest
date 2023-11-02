"""
Plot function
"""

import matplotlib.pyplot as plt

def plot_line(prediction_list, ans_list):
    """Plot for the line"""
    #plt.figure(figsize = (6, 4.5), dpi = 100)
    plt.plot(prediction_list, label='prediction')
    plt.plot(ans_list, label='true value')
    
    print(ans_list)
    plt.axhline(y = ans_list[0], color = 'gray', linestyle = '-')
    plt.xlabel('days')
    plt.ylabel('price')
    plt.legend()
    plt.show()