from node import Node


class Stack():
    def __init__(self):
        self.top = None
        self.size = 0

    def __repr__(self):
        return 'The stack has {num} Nodes, and {top} is at the top'.format(
            num=self.size, top=self.top)

    def _size(self):
        return self.size

    def push(self, val):
        '''Add a value to the head of the stack.
            args:
                val: The value to add to the stack'''
        if self.top is None:
            self.top = Node(val)
        else:
            temp = self.top
            self.top = Node(val)
            temp.next = self.top
            self.top.prev = temp
        self.size += 1

    def pop(self):
        '''Remove a value from head of stack and return.'''
        try:
            temp = self.top
            self.top = temp.prev
            temp.prev = None
            self.top.next = None
            self.size -= 1
            return temp.val

        except IndexError:
            return 'The stack is empty.'

    def peek(self):
        '''Returns a value from the head of the stack.'''
        return self.top.val
