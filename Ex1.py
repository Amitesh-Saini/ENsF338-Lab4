# Ex 1/1 

# It is counter intuitave to implement binary search on list as an array would handle much better
# as in binary search we need to find the middle element with arrays this is easy as it will be O(1) - arr[mid] or 
# the whole binary serach takes O(logn) time but in a list you must transverse through the list from head or tail to the middle which is  
# O(n) time making it far less efficent. 

# Ex 1/2

class node:
    def __init__(self, int_data):
        self._data = int_data
        self._next = None

    def get_data(self):
        return self._data

    def set_data(self, value):
        self._data = value

    def get_next(self):
        return self._next

    def set_next(self, nxt):
        self._next = nxt

    def to_string(self):
        return str(self._data)

 