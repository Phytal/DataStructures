class UnionFind:

    def __init__(self, size):
        if size <= 0:
            raise ValueError("Size <= 0 is not allowed")

        # the number of elements in this union find
        # tracks the number of components in the union find
        self.size = size
        self.num_components = size
        # used to track the sizes of each of the components
        # id[i] points to the parent of i, if id[i]  i the i is a root node
        self.sz = [0] * size
        self.id = [0] * size

        for i in range(size):
            self.id[i] = i
            self.sz[i] = 1

    # find which component/set 'p' belongs to, take amortized constant time
    def find(self, p):
        # find the root of the component/set
        root = p
        while root != self.id[root]:
            root = self.id[root]

        # compress the path leading back to the root.
        # doing this operation is called "path compression"
        # and is what gives us amortized constant time complexity
        while p != root:
            next_elem = self.id[p]
            self.id[p] = root
            p = next_elem

        return root

    # return whether or not the elements 'p' and
    # 'q' are in the same components/set
    def connected(self, p, q):
        return self.find(p) == self.find(q)

    # return the size of the components/set 'p' belongs to
    def component_size(self, p):
        return self.sz[self.find(p)]

    # return the number of elements in this UnionFind/Disjoint set
    def size(self):
        return self.size

    # returns the number of remaining components/sets
    def components(self):
        return self.num_components

    # unify the components.sets containing elements 'p' and 'q'
    def unify(self, p, q):
        root1 = self.find(p)
        root2 = self.find(q)

        # these elements are already in the same group!
        if root1 == root2:
            return

        # merge two components/sets together
        # merge smaller component/set into the larger one
        if self.sz[root1] < self.sz[root2]:
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2
        else:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = root1

        # since the roots found are different we know that the
        # number of components/ses has decreased by one
        self.num_components -= 1
