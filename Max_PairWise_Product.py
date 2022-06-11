def max_pairwise_product(nums):
    '''
    This function for returning the largest value produced by multiplying two numbers in a list of numbers.
    INPUT:
    nums: lst. A list of numbers.
    OUTPUT:
    The largest value produced by multiplying two numbers.
    '''
    lnth=len(nums)
    max_val=0
    for i in range(lnth):
        for j in range(i+1,lnth):
            max_val=max(max_val,nums[i]*nums[j])
    return max_val

if __name__ == '__main__':
    n=int(input())
    inputs=[int(i) for i in input().split()]
    print(max_pairwise_product(inputs))