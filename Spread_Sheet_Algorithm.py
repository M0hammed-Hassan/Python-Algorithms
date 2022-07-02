def spread_sheet_column(col_str):
    '''
    This function for returning the number of the column string in the spread sheet.
    INPUT:
    col_str: str. The column name in the spread sheet.
    OUTPUT:
    The number of the column. 
    '''
    num = 0
    cnt = len(col_str) - 1
    for s in col_str:
        num += 26 ** cnt * (ord(s) - ord('A') + 1)
        cnt -= 1
    return num

if __name__ == '__main__':
    string = input()
    print(spread_sheet_column(string))
