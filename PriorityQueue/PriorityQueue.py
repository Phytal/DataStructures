# A min priority queue implementation using a binary heap
import bisect


class PQueue:
    # the number of elements currently inside the heap
    heap_size = 0
    # the internal capacity of the heap
    heap_capacity = 0
    # a dynamic list to track the elements inside the heap
    heap = list()

    # this map keeps track of the possible indices a particular
    # node value is found in the heap. Having this mapping lets us
    # have 0(log(n)) removals and 0(1) element containment check at
    # the cost of some additional space and minor overhead
    map = dict()

    # construct a priority queue using heapify in 0(n) time
    def __init__(self, size=1, elems=None):
        if elems is not None:
            self.heap_size = self.heap_capacity = len(elems)
            # self.heap = [None] * self.heap_capacity

            # place all elements in heap
            for i, elem in enumerate(elems):
                self._mapAdd(elem, i)
                self.heap.append(elem)

            # heapify process, 0(n)
            i = int(max(0, (self.heap_size / 2) - 1))
            while i >= 0:
                self._sink(i)
                i -= 1
        else:
            self.heap = [None] * size

    # returns true/false depending on if th priority queue is empty
    def isEmpty(self):
        return self.heap_size == 0

    # clears everything inside the heap, 0(n)
    def clear(self):
        for i in range(self.heap_capacity):
            self.heap[i] = None
        self.heap_size = 0
        self.map.clear()

    # return the size of the heap
    def size(self):
        return self.heap_size

    # returns the value of the element with the lowest
    # priority in this priority queue. If the priority
    # queue is empty None is returned
    def peek(self):
        if self.isEmpty():
            return None
        return self.heap[0]

    # removes the root of the heap, 0(log(n))
    def poll(self):
        return self._removeAt(0)

    # test if an element is in heap, 0(1)
    def __contains__(self, item):
        if item is None:
            return False
        return self.map.get(item) is not None

    # adds an element to the priority queue, the
    # element must not be null, 0(log(n))
    def add(self, item):
        if item is None:
            raise ValueError()
        if self.heap_size < self.heap_capacity:
            self.heap[self.heap_size] = item
        else:
            self.heap.append(item)
            self.heap_capacity += 1

        self._mapAdd(item, self.heap_size)

        self._swim(self.heap_size)
        self.heap_size += 1

    # tests if the value of node i <= node j
    # this method assumes i and j are valid indices, 0(1)
    def _less(self, i, j):
        node1 = self.heap[i]
        node2 = self.heap[j]
        return node1 <= node2

    # bottom up node swim, 0(log(n))
    def _swim(self, k):
        # grab the index of the next parent node WRT to k
        parent = int((k - 1) / 2)

        # keep swimming while we have not reached the
        # root and while we're less than our parent
        while k > 0 and self._less(k, parent):
            # exchange k with the parent
            self._swap(parent, k)
            k = parent

            # grab the index of the parent node WRT to k
            parent = int((k - 1) / 2)

    # top down node sink, 0(log(n))
    def _sink(self, k):
        while True:
            left = 2 * k + 1  # left node
            right = 2 * k + 2  # right node
            smallest = left  # assume left is the smallest node of the two children

            # find which is smaller left or right
            # if right is smaller set smallest to be right
            if right < self.heap_size and self._less(right, left):
                smallest = right

            # stop if we're outside the bounds of the tree
            # or stop early if we cannot sink k anymore
            if left >= self.heap_size or self._less(k, smallest):
                break

            # move down the tree following the smallest node
            self._swap(smallest, k)
            k = smallest

    # swap two nodes. Assumes i and j are valid 0(1)
    def _swap(self, i, j):
        i_elem = self.heap[i]
        j_elem = self.heap[j]

        self.heap[i] = j_elem
        self.heap[j] = i_elem

        self._mapSwap(i_elem, j_elem, i, j)

    # removes a particular element in the heap, 0(log(n))
    def remove(self, element):
        if element is None:
            return False
        # logarithmic removal with map, 0(log(n))
        index = self._mapGet(element)
        if index is not None:
            self._removeAt(index)
        return index is not None

    # removes a node at a particular index, 0(log(n))
    def _removeAt(self, i):
        if self.isEmpty():
            return None
        self.heap_size -= 1
        removed_data = self.heap[i]
        if self.heap_size > 0:
            self._swap(i, self.heap_size)

        # obliterate the value
        self.heap.pop(self.heap_size)
        self._mapRemove(removed_data, self.heap_size)

        # removed last element
        if i is self.heap_size:
            return removed_data

        elem = self.heap[i]

        # try sinking element
        self._sink(i)

        # if sinking did not work try swimming
        if self.heap[i] is elem:
            self._swim(i)

        return removed_data

    # recursively checks if this heap is a min heap
    # this method is just for testing purposes to make
    # sure the heap invariant is still being maintained
    # called this method with k=0 to start at the root
    def isMinHeap(self, k):
        # if we are outside the bounds of the heap return true
        if k >= self.heap_size:
            return True

        left = 2*k+1
        right = 2*k+2

        # make sure that the current node k is less than
        # both of its children left, and right if they exist
        # return false otherwise to indicate an invalid heap
        if left < self.heap_size and not self._less(k, left):
            return False
        if right < self.heap_size and not self._less(k, right):
            return False

        # recurse on both children to make sure they're also valid heaps
        return self.isMinHeap(left) and self.isMinHeap(right)

    # add a node value and its index to the map
    def _mapAdd(self, value, index):
        set = self.map.get(value)

        # new value being inserted in map
        if set is None:
            set = []
            bisect.insort(set, index)
            self.map[value] = set

        # value already exists in map
        else:
            set.append(index)

    # removes the index at a given value 0(log(n))
    def _mapRemove(self, value, index):
        set = self.map.get(value)
        set.remove(index)
        if len(set) == 0:
            self.map.pop(value)

    # extract an index position for the given value
    # NOTE: if a value exists multiple times in the heap the highest
    # index is returned (this has arbitrarily been chosen)
    def _mapGet(self, value):
        set = self.map.get(value)
        if set is not None:
            return set[-1]
        return None

    # exchange the index of two nodes internally within the map
    def _mapSwap(self, val1, val2, val1_index, val2_index):
        set1 = self.map.get(val1)
        set2 = self.map.get(val2)

        set1.remove(val1_index)
        set2.remove(val2_index)

        set1.append(val2_index)
        set2.append(val1_index)

    def __repr__(self):
        return str(self.heap)
