def solution():
    tall_0 = list(map(int, input().split(",")))
    res = 0
    tall_1 = tall_0.copy()
    tall_0.sort()

    for i in range(len(tall_0)):
        if tall_0[i] != tall_1[i]:
            res += 1

    print(res)

if __name__ == "__main__":
    print(solution())