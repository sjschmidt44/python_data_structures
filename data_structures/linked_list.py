class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return '{val}'.format(val=self.val)


class LinkedList(object):
    def __init__(self, values=None, head=None):
        self.head = head
        self.length = 0

    def __repr__(self):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def size(self):
        pass

    def search(self):
        pass

    def display(self):
        pass

    def remove(self):
        pass

    def insert(self):
        pass

    def pop(self):
        pass
