def intersect_sorted_list(a,b):
    '''
    This function for finding the intersection between two lists.
    INPUT:
    a1: list. The first list.
    a2: list. The second list.
    OUTPUT:
    Common items in the two lists.
    '''
    i = 0
    j = 0
    common_items = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            if i == 0 or a[i] != a[i-1]:    
                common_items.append(a[i])
            i += 1
            j += 1
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1
    return common_items

if __name__ == '__main__':
    a = list(map(int,input().split(' ')))
    b = list(map(int,input().split(' ')))
    print(intersect_sorted_list(a,b))