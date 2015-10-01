from node import Node


class LinkedList(object):
    def __init__(self, iterable=()):
        self._current = None
        self.head = None
        self.length = 0
        for val in reversed(iterable):
            self.insert(val)

    def __repr__(self):
        '''Print string representation of Linked List.'''
        node = self.head
        output = ''
        for node in self:
            output += '{!r}'.format(node.val)
        return '({})'.format(output.rstrip(' ,'))

    def __len__(self):
        return self.length

    def __iter__(self):
        if self.head is not None:
            self._current = self.head
        return self

    def next(self):
        if self._current is None:
            raise StopIteration
        node = self._current
        self._current = self._current.next
        return node

    def insert(self, val):
        '''Insert new Node at head of Linked List.'''
        self.head = Node(val, self.head)
        self.length += 1
        return None

    def pop(self):
        '''Pop the first Node from the head of Linked List, return val'''
        if self.head is None:
            raise IndexError
        else:
            to_return = self.head
            self.head = to_return.next
            self.length -= 1
            return to_return.val

    def size(self):
        '''Return current length of Linked List.'''
        return len(self)

    def search(self, search):
        '''Return given node of Linked List if present, else None.'''
        for node in self:
            if node.val == search:
                return node
        else:
            return None

    def remove(self, search):
        '''Remove given node from Linked List, return None.'''
        for node in self:
            if node.next == search:
                node.next = node.next.next
                return None

    def display(self):
        '''Display Linked List as string.'''
        return repr(self)
