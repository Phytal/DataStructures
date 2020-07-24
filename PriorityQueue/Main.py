import PriorityQueue


def main():
    pq = PriorityQueue.PQueue(elems=[1, 2, 3, 4, 4, 5, 6, 7, 33, 55, 564, 7658, 2233, 9, 44, 5, 33, 34])
    print(pq)
    pq.add(44)
    pq.add(23)
    result = []

    while not pq.isEmpty():
        result.append(pq.poll())

    print(pq)
    print(result)


if __name__ == "__main__":
    main()
