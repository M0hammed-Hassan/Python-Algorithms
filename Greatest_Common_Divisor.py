def gcd(n1,n2):
    '''
    This function for implementing the Euclidean algorithm for computing
    the greatest common divisor.
    INPUT:
    n1: int. Non negative number.
    n2: int. Non negative number.
    OUTPUT:
    The greatest common divisor.
    '''
    if n1==0:
        print(n2)
    if n2==0:
        print(n1)
    res=n1%n2
    if res==0:
        print(n2)
    else:
        gcd(n2,res)

if __name__ == "__main__":
    a,b=map(int,input().split())
    gcd(a,b)