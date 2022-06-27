#Linear Search
from msilib.schema import Billboard


def linear_search(data,target):
    '''
    This function for implementing linear search algorithm.
    INPUT:
    data: list. A list of elements.
    target: (str,int,..etc). An element for searching it.
    OUTPUT:
    True(When the element exist) or False(When the element not exist).
    '''
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

#Binary Search
def binary_search(data,target):
    '''
    This function for implementing binary search algorithm.
    INPUT:
    data: list. A list of elements.
    target: (str,int,..etc). An element for searching it.
    OUTPUT:
    True(When the element exist) or False(When the element not exist).
    '''
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

if __name__ == '__main__':
    data = [10,15,25,26,30,36,38,49,80,109]
    print(linear_search(data,90))
    print(binary_search(data,26))