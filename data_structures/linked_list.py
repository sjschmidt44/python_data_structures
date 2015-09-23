class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return '{val}'.format(val=self.val)


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

    def insert(self):
        pass

    def size(self):
        pass

    def search(self):
        pass

    def display(self):
        pass

    def remove(self):
        pass

    def pop(self):
        pass
