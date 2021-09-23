if __name__ == '__main__':
    num = int(input())
    for _ in range(num):  # 每组测试用例
        horseNum = int(input())
        horseList = list(map(int, input().split()))
        horseList.sort()
        if horseList[horseNum-1] < horseList[horseNum]:
            print("YES")
        else:
            print("NO")
