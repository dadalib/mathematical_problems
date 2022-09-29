

import numpy as np

def odd_numbers_first(values):
    odd_array =[]
    not_odd_array=[]
    sum_array = []

    for value in values:
        if value%2 ==0:
            odd_array.append(value)
        
        else:
            not_odd_array.append(value)
    sum_array = sorted(odd_array) + sorted(not_odd_array)
    return  sum_array

def flip_horizontally(values):
    return values[::-1]

def get_dimension(values2dim):
    if isinstance(values2dim,list):
        print("Manual array")
        return (len(values2dim),len(values2dim[0]))

    if isinstance(values2dim,np.ndarray):
        print("Numpy array")
        return values2dim.shape

    raise ValueError("unsupported type",type(values2dim))



    
if __name__ == "__main__":
    # print(odd_numbers_first([2, 4, 6, 8, 1]))
    # print(flip_horizontally([1,2,3,4]))
    a2D = np.array([[1,2],[3,2]])
    array =[[1, 2, 3], [4, 5, 6],[7, 8, 9]]

    print(get_dimension(a2D))