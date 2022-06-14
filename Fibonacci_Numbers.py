def fibonacci_alg(n):
    '''
    This function for implementing fibonacci algorithm.
    INPUT:
    n: int. The fibonacci number.
    OUTPUT:
    The value of the given fibonacci number.
    '''
    if n<=1:
        return n
    f=[]
    f.append(0)
    f.append(1)
    n=n+1
    for i in range(2,n):
        f.append((f[i-1]+f[i-2]))
    return f[n-1]

if __name__ == '__main__':
    num=int(input())
    print(fibonacci_alg(num))