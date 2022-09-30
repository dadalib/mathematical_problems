

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
        print("Using manually")
        return (len(values2dim),len(values2dim[0]))

    if isinstance(values2dim,np.ndarray):
        print("Numpy array")
        print("Usin numpy dimension")
        return values2dim.shape

    raise ValueError("unsupported type",type(values2dim))

def swap(values,first,second):
    buffer = values[first]
    values[first]=values[second]
    values[second] = buffer

    return values



def flip_horizontally_v2(values2dim):
    max_y,max_x = get_dimension(values2dim)
    print("max_y",max_y)
    print("max_y",max_y)

    for y in range(max_y):
        print("y",y)
        row = values2dim[y]
        print("row",row)
        for x in range(max_x // 2):
            print("x",x)
            print("max_x // 2" ,max_x // 2)
            swap(row,x,max_x - x - 1)

def flip_vertically_just_for_lists(values2dim):
    max_y, _= get_dimension(values2dim)
    print("max_y",max_y)
    print("max_y//2",max_y // 2)
    for y in range(max_y // 2):
        print("y",y)
        results =swap(values2dim,y,max_y - y -1)

    return results





    
if __name__ == "__main__":
    # print(odd_numbers_first([2, 4, 6, 8, 1]))
    # print(flip_horizontally([1,2,3,4]))
    a2D = np.array([[1,2,4],
                    [3,2,7],
                    [4,7,3],
                    ])

    array =[[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    # print(get_dimension(a2D))
    # print(flip_horizontally_v2(a2D))
    print(flip_vertically_just_for_lists(a2D))