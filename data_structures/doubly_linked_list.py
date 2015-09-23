class Node(object):
    def __init__(self, val, prev=None, next_=None):
        self.val = val
        self.prev = prev
        self.next = next_

    def __repr__(self):
        return '{val}'.format(val=self.val)


class DoublLinkedList(object):
    def __init__(self, iterable=()):
        self._current = None
        self.head = None
        self.tail = None
        self.length = 0
        for val in reversed(iterable):
            self.insert(val)

    def __repr__(self):
        node = self.head
        output = ''
        for node in self:
            output += '{!r}, '.format(node.val)
        return '({})'.format(output.rstrip(' ,'))

    def __len__(self):
        return self.length

    def __iter__(self):
        if self.head is not None:
            self._current = self.head
        return self

    def next(self):
        pass

    def size(self):
        pass

    def search(self, search):
        pass

    def remove(self, search):
        pass

    def insert(self, val):
        pass

    def append(self, val):
        pass

    def pop(self):
        pass

    def shift(self):
        pass

    def display(self):
        ''''''
        return repr(self)
