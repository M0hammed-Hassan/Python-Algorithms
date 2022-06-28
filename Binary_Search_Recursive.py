def binary_search_recursive(data,target,low,high):
    '''
    This function for implementing binary search algorithm by using recursive technique.
    INPUT:
    data: list. A list of elements.
    target: (str,int,..etc). An element for searching it.
    low: int. The low value.
    high: int. The high value.
    OUTPUT:
    True(When the element exist) or False(When the element not exist).
    '''
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data,target,low,mid - 1)
        else:
            return binary_search_recursive(data,target,mid + 1,high)

if __name__ == '__main__':
    data = [5,50,60,85,89,209,804,1099,2000,2015,2300,8000,50000]
    target = 2300
    print(binary_search_recursive(data,target,0,len(data)-1))

