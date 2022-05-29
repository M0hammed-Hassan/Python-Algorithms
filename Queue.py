#Creating a class
class Queue():
    def __init__(self):
        '''
        This is the initialize method for the class,
        it contains the instance attributes.
        '''
        self.items=[]
    def size(self):
        '''
        This method for returning the size of the queue.
        '''
        return len(self.items)
    def is_empty(self):
        '''
        This method returns a boolean value,
        it returns True if the queue is empty
        and it returns False if the queue isn't empty.
        '''
        return self.items == []
    def enqueue(self,item):
        '''
        This method for adding an item in the rear.
        INPUT:
        item:  (str,integer,...etc). An item for storing it in the queue.
        '''
        self.items.insert(0,item)
    def dequeue(self):
        '''
        This method for removing an item in the front.
        OUTPUT:
        The removed item.
        '''
        return self.items.pop()