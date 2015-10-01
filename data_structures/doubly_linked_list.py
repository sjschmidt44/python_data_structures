from node import Node


class DoublyLinkedList(object):
    '''Doubly Linked List class object.'''
    def __init__(self, iterable=()):
        self._current = None
        self.head = None
        self.tail = None
        self.length = 0
        for val in reversed(iterable):
            self.insert(val)

    def __repr__(self):
        '''Return string representation of Doubly Linked List.'''
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
        if self._current is None:
            raise StopIteration
        node = self._current
        self._current = self._current.next
        return node

    def size(self):
        '''Return the length of Doubly Linked List.'''
        return len(self)

    def search(self, search):
        '''Return node if present in Doubly Linked List, else None.'''
        for node in self:
            if node.val == search:
                return node
        else:
            return None

    def remove(self, search):
        '''Remove node from Doubly Linekd List if present, else raise
        ValueError.'''
        search_node = self.search(search)

        if search_node == self.head:
            self.head = search_node.next
            try:
                self.head.prev = None
            except AttributeError:
                pass
            self.length -= 1
        elif search_node == self.tail:
            self.tail = search_node.prev
            try:
                self.tail = search_node.prev
            except AttributeError:
                pass
            self.length -= 1
        else:
            for node in self:
                if node == search_node:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    self.length -= 1
                    return None
            raise ValueError('Value not in list.')

    def insert(self, val):
        '''Insert node at the head of Doubly Linked list.'''
        old_head = self.head
        self.head = Node(val, prev=None, next_=old_head)
        if old_head is None:
            self.tail = self.head
        else:
            old_head.prev = self.head
        self.length += 1
        return None

    def append(self, val):
        '''Insert node at the tail of Doubly Linked List.'''
        old_tail = self.tail
        self.tail = Node(val, prev=old_tail, next_=None)
        if old_tail is None:
            self.head = self.tail
        else:
            old_tail.next = self.tail
        self.length += 1
        return None

    def pop(self):
        '''Remove node at the head of the Doubly Linked List.'''
        if self.head is None:
            raise IndexError('pop from empty list')
        else:
            to_return = self.head
            self.head = to_return.next
            try:
                self.head.prev = None
            except AttributeError:
                self.tail = None
            self.length -= 1
            return to_return.val

    def shift(self):
        '''Remove node at the tail of the Doubly Linked List.'''
        if self.tail is None:
            raise IndexError('pop from empty list')
        else:
            to_return = self.tail
            self.tail = to_return.prev
            try:
                self.tail.next = None
            except AttributeError:
                self.head = None
            self.length -= 1
            return to_return.val

    def display(self):
        '''Return the node values of Doubly Linked List as string.'''
        return repr(self)
