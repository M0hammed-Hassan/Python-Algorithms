#Creating deque class
class Deque():
    def __init__(self):
        '''
        This is the initialize method for the class,
        it contains the instance attributes.
        '''
        self.items=[]
    def addFront(self,item):
        '''
        This method for adding an item in the front.
        INPUT:
        item: (str,integer,...etc). An item for storing it in the deque.
        '''
        self.items.append(item)
    def addRear(self,item):
        '''
        This method for adding an item in the rear.
        INPUT:
        item: (str,integer,...etc). An item for storing it in the deque.
        '''
        self.items.insert(0,item)
    def removeFront(self):
        '''
        This method for removing an item from the front.
        OUTPUT:
        The removed item.
        '''
        return self.items.pop()
    def removeRear(self):
        '''
        This method for removing an item from the rear.
        OUTPUT:
        The removed item.
        '''
        return self.items.pop(0)
    def size(self):
        '''
        This method for returning the size of the deque.
        OUTPUT:
        The size of the deque.
        '''
        return len(self.items)
    def isEmpty(self):
        '''
        This method for returning an boolean value.
        OUTPUT:
        True or False.
        '''
        return self.items == []