from typing import Generic, TypeVar
from LinkedLists import LinkedList

T = TypeVar('T')


class Stack(Generic[T]):

    # create an empty stack
    def __init__(self, firstElem):
        self.linked_list = LinkedList.DoublyLinkedList()
        if firstElem is not None:
            self.push(firstElem)

    # return the number of elements in the stack
    def size(self):
        return self.linked_list.size

    # check if the stack is empty
    def isEmpty(self):
        return self.size() == 0

    # push an element on the stack
    def push(self, elem):
        self.linked_list.addLast(elem)

    # pop an element off the stack
    # throws an error if the stack is empty
    def pop(self):
        if self.isEmpty():
            raise StackError("Stack is empty!")
        return self.linked_list.removeLast()

    # peek the top of the stack without removing an element
    # throws an error if the stack is empty
    def peek(self):
        if self.isEmpty():
            raise StackError("Stack is empty!")
        return self.linked_list.peekLast()

    def __repr__(self):
        output = '[ '
        trav = self.linked_list.head
        while trav is not None:
            output += str(trav.data) + ', '
            trav = trav.next
        output = output[:-2]
        output += ' ]'
        return output


class StackError(Exception):
    pass
