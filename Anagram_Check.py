def anagram(s1,s2):
    '''
    This function check if two strings are anagram.
    INPUT:
    s1: str. The first string.
    s2: str. The second string.
    OUTPUT:
    True or False
    '''
    #Removing spaces
    #Converting all uppercase letters to lowercase
    s1=s1.replace(' ','').lower()
    s2=s2.replace(' ','').lower()
    
    #Checking the length
    if len(s1) != len(s2):
        return False
    
    #Creating dictionary
    cnt={}
    
    #Adding the counts
    for letter in s1:
        if letter in cnt:
            cnt[letter]+=1
        else:
            cnt[letter]=1
    
    #Subtracting counts
    for letter in s2:
        if letter in cnt:
            cnt[letter]-=1
        else:
            cnt[letter]=1
    
    #Checking if all counts equal to zero
    for k in cnt:
        if cnt[k]!=0:
            return False
    return True