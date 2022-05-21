#Library
import ctypes
#Creating DynamicArray class
class DynamicArray():
    def __init__(self):
        '''
        This is the initialize method for the class, it
        contains the instance attributes.
        '''
        self.cnt=0
        self.capacity=1
        self.a=self.create_array(self.capacity)
    def len(self):
        '''
        This method for obtaining the length of the array.
        OUTPUT:
        Array length.
        '''
        return self.cnt
    def get_item(self,index):
        '''
        This method for getting an item by using it's index.
        INPUT:
        index: int. The index of an item. 
        OUTPUT:
        A specific item from the array.
        '''
        if not 0<=index<self.cnt:
            return IndexError("This index out of range.")
        return self.a[index]
    def append(self,val):
        '''
        This method for appending an item at the end of
        the array.
        INPUT:
        val: str,int,...etc. The value to append in the array.
        '''
        if self.cnt == self.capacity:
            self._resize(2*self.capacity)
        self.a[self.cnt]=val
        self.cnt+=1
    def _resize(self,new_capacity):
        '''
        This method for resizing the array.
        INPUT:
        new_capacity: int. This is a new capacity for the array.
        '''
        b=self.create_array(new_capacity)
        for i in range(self.cnt):
            b[i]=self.a[i]
        self.a=b
        self.capacity=new_capacity
    def create_array(self,capacity):
        '''
        This method for creating array capacity.
        OUTPUT:
        Array with a specific capacity.
        '''
        return (capacity*ctypes.py_object)()