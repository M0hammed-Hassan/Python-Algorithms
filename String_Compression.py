def compress(s):
    '''
    This function for compressing a string.
    INPUT:
    s: str. The string.
    OUTPUT:
    Compressed string.
    '''
    
    #Checking the length with zero
    length=len(s)
    if length == 0:
        return
    
    #Checking the length with one
    if length == 1:
        return s+"1"
    
    #Defining required variables 
    res=""
    index=1
    cnt=1
    
    #While the index less than the length of the string
    while index < length:
        
        #Checking if the current index equal to the previous one
        if s[index]==s[index-1]:
            
            #Increment the count
            cnt+=1
            
        #Storing the results
        else:
            res=res+s[index-1]+str(cnt)
            
            #Assign the count with one
            cnt=1
            
        #Increment the index
        index+=1
        
    #Returning the last result
    res=res+s[index-1]+str(cnt)
    return res