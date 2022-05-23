def sentence_reversal(s):
    '''
    This function for splitting a sentence then reverse it.
    INPUT:
    s. str. The sentence.
    OUTPUT:
    The reverse of the given sentence.
    '''
    
    #The length of the sentence
    length=len(s)
    
    #A list for storing the words
    words=[]
    
    #The index
    i=0
    
    #While the index less than the length
    while i<length:
        
        #If the element isn't a space
        if s[i] != ' ':
            
            #The word starts from this index
            word_start=i
            
            #While the index less than the length and the element isn't a space
            while i<length and s[i] != ' ':
            
                #Increment the index
                i+=1
            
            #Appending the words    
            words.append(s[word_start:i])
        
        #Increment the index
        i+=1
        
    #Joining the reversed words
    return " ".join(reversed(words))