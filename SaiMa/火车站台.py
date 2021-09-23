if __name__ == '__main__':
    num = int(input())
    CityList = [0] * 10000
    for i in range(num):
        List = list(map(int, input().split(" ")))
        for city in range(List[0], List[1]):
            CityList[city] += 1

    print(max(CityList))
