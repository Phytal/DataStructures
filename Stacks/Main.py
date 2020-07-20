from Stacks import Stack


def main():
    stack = Stack.Stack(None)
    stack.push("1")
    stack.push("2")
    stack.push("3")
    print(stack)
    stack.pop()
    print(stack.peek())
    print(stack)


if __name__ == '__main__':
    main()
