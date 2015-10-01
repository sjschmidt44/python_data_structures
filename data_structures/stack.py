from node import Node


class Stack():
    '''First in, Last out. Aware of top of stack only.'''
    def __init__(self):
        pass

    def __repr__(self):
        return repr(self)

    def __iter__(self):
        if self.head is not None:
            self._current = self.head
        return self

    def push(self, value):
        '''Add a value to the head of the stack.
            args:
                value: The value to add to the stack'''

        '''When push; set head in temp. assign new node to head.
        head pointer to new node.'''
        pass

    def pop(self):
        '''Remove a value from head of stack and return.'''

        '''When Pop; '''

        pass

    def peek(self):
        '''Returns a value from the head of the stack.'''
        pass
