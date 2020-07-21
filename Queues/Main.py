from Queues import Queue
from Queues import Queue2


class Node:
    def __init__(self, data, neighbors):
        self.visited = False
        self.data = data
        self.neighbors = neighbors


# breadth first search
# there's probably an easier way but i just winged it
def main():
    graph = []
    h = Node("h", [])
    g = Node("g", [])
    f = Node("f", [])
    e = Node("e", [h])
    d = Node("d", [e, f, g])
    c = Node("c", [d])
    b = Node("b", [d])
    a = Node("a", [b, c])
    graph.extend((a, b, c, d, e, f, g, h))
    starting_node = graph[0]
    q = Queue.Queue()
    q.offer(starting_node)
    starting_node.visited = True

    while q.isEmpty() is not True:
        node = q.poll()

        for neighbor in node.neighbors:
            if neighbor.visited is False:
                neighbor.visited = True
                print(neighbor.data)
                q.offer(neighbor)


if __name__ == '__main__':
    main()
