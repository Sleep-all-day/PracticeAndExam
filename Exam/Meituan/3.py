def myinput():
    n, m = map(int, input().split())
    array = []
    for i in range(n + 1):
        array.append([])

    for i in range(m):
        first, second = map(int, input().split())
        array[first].append(second)
        array[second].append(first)

    return array


def solution(mylist):
    reslist = []
    backtrack = []

    for i, num in enumerate(mylist):
        if (len(num)) > 0:
            backtrack.append(i)
            for k, l in enumerate(num):
                if l not  in backtrack:
                    backtrack.append(l)
                    mydfs(mylist, l, reslist, backtrack)
                    backtrack.pop()
            backtrack.pop()
    return len(reslist)


def mydfs(mylist, l, reslist, backtrack):
    if len(backtrack) > 5:
        return
    if len(backtrack) == 5:
        temp = []
        for _ in backtrack:
            temp.append(_)
        temp.sort()
        if temp not in reslist:
            reslist.append(temp)

    _list = mylist[l]
    for i, j in enumerate(_list):
        if j not in backtrack:
            backtrack.append(j)
            mydfs(mylist, j, reslist, backtrack)
            backtrack.pop()


if __name__ == '__main__':
    mylist = myinput()
    print(solution(mylist))
