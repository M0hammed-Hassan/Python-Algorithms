#Creating stack class
class Stack():
    def __init__(self):
        '''
        This is the initialize method for the class,
        it contains the instance attributes.
        '''
        self.items=[]
    def push(self,item):
        '''
        This method for appending an item into the top of the stack.
        INPUT:
        item: (str,integer,...etc). An item for storing it in the stack.
        '''
        
        self.items.append(item)
    def pop(self):
        '''
        This method for removing an item from the top of the stack.
        OUTPUT:
        Removed item.
        '''
        return self.items.pop()
    def peek(self):
        '''
        This method for returning the top item from the stack.
        OUTPUT:
        The top item.
        '''
        return self.items[len(self.items)-1]
    def size(self):
        '''
        This method for returning the size of the stack.
        OUTPUT:
        The size of the stack.
        '''
        return len(self.items)
    def is_empty(self):
        '''
        This method for checking if the stack is empty or not.
        OUTPUT:
        A boolean value.
        '''
        return self.items == []