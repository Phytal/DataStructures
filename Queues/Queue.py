from typing import Generic, TypeVar
from LinkedLists import LinkedList

T = TypeVar('T')


class Queue(Generic[T]):
    llist = LinkedList.DoublyLinkedList()

    def __init__(self, first_elem=None):
        if first_elem is not None:
            self.offer(first_elem)

    # return the size of the queue
    def size(self):
        return self.llist.size

    def isEmpty(self):
        return self.size() == 0

    # peek the element at the front of the queue
    # the method throws an error if the queue is empty
    def peek(self):
        if self.isEmpty():
            raise QueueError("Queue is empty!")
        return self.llist.peekFirst()

    # poll an element from the front of the queue
    # the method throws an error if the queue is empty
    def poll(self):
        if self.isEmpty():
            raise QueueError("Queue is empty!")
        return self.llist.removeLast()

    # add an element to the back of the queue
    def offer(self, elem):
        self.llist.addLast(elem)


class QueueError(Exception):
    pass
