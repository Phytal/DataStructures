from LinkedLists import LinkedList


def main():
    data1 = "hello"
    data2 = "I"
    data3 = "am"
    data4 = "your"
    data5 = "father"
    data6 = "luke"
    data7 = "skywalker"

    linked_list = LinkedList.DoublyLinkedList()
    linked_list.add(data1)
    linked_list.add(data2)
    linked_list.add(data3)
    linked_list.add(data4)
    linked_list.add(data5)
    linked_list.add(data6)
    linked_list.add(data7)

    print(linked_list)

    linked_list.removeFirst()
    linked_list.removeLast()

    print(linked_list)

    print(linked_list.contains("your"))
    print(linked_list.peekLast())


if __name__ == '__main__':
    main()
