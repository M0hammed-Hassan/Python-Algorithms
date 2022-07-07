def is_palin_perm(string):
    '''
    This function to check if the given string is a permutation of a palindrome.
    INPUT:
    string: str. The input string.
    OUTPUT:
    True if the given string is a permutation of a palindrome, otherwise False.
    '''
    string = string.replace(' ','').lower()
    dic = {}
    for letter in string:
        if letter in dic:
            dic[letter] += 1
        else:
            dic[letter] = 1
    odd_cnt = 0
    for k,v in dic.items():
        if v % 2 != 0 and odd_cnt == 0:
            odd_cnt += 1
        elif v % 2 != 0 and odd_cnt != 0:
            return False
    return True

if __name__ == '__main__':
    input_str = input()
    print(is_palin_perm(input_str))