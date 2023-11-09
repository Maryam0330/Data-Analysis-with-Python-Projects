import numpy as np

def calculate(list):

    # Checking whether the list contains 9 digits or not
    if (len(list) != 9):
        raise ValueError("List must contain nine numbers.")
    
    # Converting the list into a 3 x 3 Numpy array
    ls = np.array(list)
    ls = ls.reshape(3,3)

    # Calculating Mean
    mean_rows = ls.mean(axis = 0)
    mean_columns = ls.mean(axis = 1)
    overall_mean = ls.mean()
    mean = [mean_rows.tolist(), mean_columns.tolist(), overall_mean]

    # Calculating Variance
    var_rows = ls.var(axis = 0)
    var_columns = ls.var(axis = 1)
    overall_var = ls.var()
    variance = [var_rows.tolist(), var_columns.tolist(), overall_var]

    # Calculating Standard Deviation
    std_rows = ls.std(axis = 0)
    std_columns = ls.std(axis = 1)
    overall_std = ls.std()
    std_deviation = [std_rows.tolist(), std_columns.tolist(), overall_std]

    # Calculating Max
    max_rows = ls.max(axis = 0)
    max_columns = ls.max(axis = 1)
    overall_max = ls.max()
    max_num = [max_rows.tolist(), max_columns.tolist(), overall_max]

    # Calculating Min
    min_rows = ls.min(axis = 0)
    min_columns = ls.min(axis = 1)
    overall_min = ls.min()
    min_num = [min_rows.tolist(), min_columns.tolist(), overall_min]

    # Calculating Sum
    sum_rows = ls.sum(axis = 0)
    sum_columns = ls.sum(axis = 1)
    overall_sum = ls.sum()
    sum_num = [sum_rows.tolist(), sum_columns.tolist(), overall_sum]


    return {
        'mean': mean,
        'variance': variance, 
        'standard deviation': std_deviation,
        'max': max_num,
        'min': min_num,
        'sum': sum_num
    }