from node import Node


class Queue(object):
    def __init__(self, tail=None, head=None):
        self.tail = tail
        self.head = head
        self.size = 0

    def __repr__(self):
        '''Return the size of the queue and node at the head of the queue.'''
        return 'The Queue has {num} nodes, with {head} at the head.'.format(
            num=self.size, head=self.head)

    def enqueue(self, val):
        '''Add new node to tail of queue.'''
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            temp = self.tail
            self.tail = Node(val)
            temp.prev = self.tail
            self.tail.next = temp
        self.size += 1

    def dequeue(self):
        '''Remove node from the head of the queue, else return empty queue.'''
        try:
            temp = self.head
            self.head = self.head.prev
            self.head.next = None
            temp.prev = None
            self.size -= 1

        except:
            return "The queue is empty."
