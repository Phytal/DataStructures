from UnionFind import UnionFind


def main():
    uf = UnionFind(10)
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    uf.unify(0, 1)
    uf.unify(2, 3)
    uf.unify(4, 5)
    uf.unify(6, 7)
    uf.unify(8, 9)
    for num in nums:
        print(num, uf.find(num))

    uf.unify(1, 3)
    uf.unify(5, 7)
    uf.unify(6, 9)

    for num in nums:
        print(num, uf.find(num))

    for num in range(uf.size):
        if uf.id[num] == 4:
            print(num)


if __name__ == "__main__":
    main()
