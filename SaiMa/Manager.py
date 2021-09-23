if __name__ == '__main__':
    num = input()
    university = list(map(int, input().split(" ")))
    university.sort(reverse=True)
    res = 0
    Len = len(university)
    if num != Len:
        print(0)

    for i in range(1, len(university)):
        while university[i] >= university[i - 1]:
            university[i] -= 1
        if university[i - 1] > 0:
            res += university[i - 1]

    if university[Len - 1] > 0:
        res += university[Len - 1]

    print(res)


