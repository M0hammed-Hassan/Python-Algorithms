def next_sequence(string):
    '''
    This function for implementing look and say sequence algorithm.
    INPUT:
    string: str. The current sequence.
    OUTPUT:
    The next sequence from the given sequence.
    '''
    res = []
    cnt = 1
    i = 0
    while i < len(string):
        while i + 1 < len(string) and string[i] == string[i+1]:
            cnt += 1
            i += 1
        res.append(str(cnt) + string[i])
        i += 1
    return ''.join(res)

if __name__ == '__main__':
    string = input()
    print(next_sequence(string))