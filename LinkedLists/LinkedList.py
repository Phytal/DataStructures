from typing import Generic, TypeVar

T = TypeVar('T')


class DoublyLinkedList(Generic[T]):
    def __init__(self):
        self.size = 0
        self.head = self.__Node(None, None, None)
        self.tail = self.__Node(None, None, None)

    class __Node:
        def __init__(self, data: T, prev, next):
            self.data = data
            self.prev = prev
            self.next = next

        def __repr__(self):
            return str(self)

    def clear(self):
        trav = self.head
        while trav is not None:
            next = trav.next
            trav.prev = trav.next = None
            trav.data = None
            trav = next
        self.head = self.tail = trav = None
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    # add an element to the tail of the linked list, 0(1)
    def add(self, elem):
        self.addLast(elem)

    # add an element to the beginning of this linked list, 0(1)
    def addFirst(self, elem):
        if self.isEmpty():
            self.head = self.tail = self.__Node(elem, None, None)
        else:
            self.head.prev = self.__Node(elem, None, self.head)
            self.head = self.head.prev

        self.size += 1

    # add an element to the tail of the linked list, 0(1)
    def addLast(self, elem):
        if self.isEmpty():
            self.head = self.tail = self.__Node(elem, None, None)
        else:
            self.tail.next = self.__Node(elem, self.tail, None)
            self.tail = self.tail.next

        self.size += 1

    # check the value of the first node if it exists 0(1)
    def peekFirst(self):
        if self.isEmpty():
            raise RuntimeError("Empty list")
        return self.head.data

    # check the value of the last node if it exists
    def peekLast(self):
        if self.isEmpty():
            raise RuntimeError("Empty list")
        return self.tail.data

    # remove the first value at the head of the linked list, 0(1)
    def removeFirst(self):
        # can't remove data from an empty list
        if self.isEmpty():
            raise RuntimeError("Empty list")

        # extract the data at the head and move the head pointer forward one node
        data = self.head.data
        self.head = self.head.next
        self.size -= 1

        # if the list is empty set the tail to null as well
        if self.isEmpty():
            self.tail = None

        # do a memory clean of the previous node
        else:
            self.head.prev = None

        # return the data that was at the first node we just removed
        return data

    # remove the last value at the tail of the linked list, 0(1)
    def removeLast(self):
        # can't remove data from an empty list
        if self.isEmpty():
            raise RuntimeError("Empty list")

        # extract the data at the tail and move the tail pointer forward one node
        data = self.tail.data
        self.tail = self.tail.prev
        self.size -= 1

        # if the list is empty set the head to null as well
        if self.isEmpty():
            self.head = None

        # do a memory clean of the node that was just removed
        else:
            self.tail.next = None

        # return the data that was at the first node we just removed
        return data

    # removed an arbitrary node from the liked list, 0(1)
    def __remove(self, node):
        # if the node to remove is somewhere either at the head orr= the tail handle those independently
        if node.prev is None:
            return self.removeFirst()
        if node.next is None:
            return self.removeLast()

        # make the pointers of adjacent nodes skip over the 'node'
        node.next.prev = node.prev
        node.prev.next = node.next

        # temporary store the data we want to return
        data = node.data

        # memory cleanup
        node.data = None
        node = node.prev = node.next = None

        self.size -= 1

        # return the data at the node we just removed
        return data

    # remove a node at a particular index, 0(n)
    def removeAt(self, index):
        # make sure the index provided is valid
        if index < 0 or index >= self.size:
            raise ValueError

        i = 0
        # search from the front of the list
        if index < self.size / 2:
            trav = self.head
            while i is not index:
                trav = trav.next
                i += 1

        # search from the back of the list
        else:
            trav = self.tail
            i = self.size
            while i is not index:
                trav = trav.prev

        return self.__remove(trav)

    # remove a particular value in the linked list, 0(n)
    def remove(self, obj):
        trav = self.head

        # support searching for None
        if obj is None:
            while trav is not None:
                if trav.data is None:
                    self.__remove(trav)
                    return True
                trav = trav.next
        # search for non-null object
        else:
            while trav is not None:
                if obj is trav.data:
                    self.__remove(trav)
                    return True
                trav = trav.next
        return False

    # find the index of a particular value in the linked list, 0(n)
    def indexOf(self, obj):
        index = 0
        trav = self.head

        # support searching for None
        if obj is None:
            while trav is not None:
                if trav.data is None:
                    return index
                index += 1
                trav = trav.next
        # search for non-null object
        else:
            while trav is not None:
                if obj is trav.data:
                    return index
                index += 1
                trav = trav.next
        return -1

    # check if a value is contained within the linked list
    def contains(self, obj):
        return self.indexOf(obj) != -1

    def __repr__(self):
        output = '[ '
        trav = self.head
        while trav is not None:
            output += trav.data + ', '
            trav = trav.next
        output = output[:-2]
        output += ' ]'
        return output
