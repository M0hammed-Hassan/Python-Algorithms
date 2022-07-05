def is_palindrome(string):
    '''
    This function for checking if the string is palindrome or not.
    INPUT:
    string: str. The input string.
    OUTPUT:
    True if the string is palindrome, and false if the string is not palindrome.
    '''
    i = 0
    j = len(string) - 1
    while i < j:
        while not string[i].isalnum() and i < j:
            i += 1
        while not string[j].isalnum() and i < j:
            j -= 1
        if string[i].lower() != string[j].lower():
            return False

        i += 1
        j -= 1
    return True

if __name__ == '__main__':
    input_str = input()
    print(is_palindrome(input_str))