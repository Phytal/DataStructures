from typing import Generic, TypeVar
from Queues import Queue

T = TypeVar('T')


# note: python makes this too easy
class Queue2(Generic[T]):
    array_list = []

    def __init__(self, firstElem):
        if firstElem is not None:
            self.offer(firstElem)

    # return the size of the queue
    def size(self):
        return len(self.array_list)

    def isEmpty(self):
        return self.size() == 0

    # peek the element at the front of the queue
    # the method throws an error if the queue is empty
    def peek(self):
        if self.isEmpty():
            raise Queue.QueueError("Queue is empty!")
        return self.array_list[self.size() - 1]

    # add an element to the back of the queue
    def offer(self, elem):
        self.array_list.append(elem)

    # poll an element from the front of the queue
    # the method throws an error if the queue is empty
    def poll(self):
        if self.isEmpty():
            raise Queue.QueueError("Queue is empty!")
        self.array_list.pop()

