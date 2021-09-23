if __name__ == '__main__':
    questions = int(input())
    for question in range(questions):
        nums = int(input())
        List = []
        for everyone in range(nums):
            List.append(list(map(int, input().split(" "))))

        CurList = []
        for i in range(nums):
            for _ in List[i]:
                if _ not in CurList:
                    CurList.append(_)
                else:
                    CurList.remove(_)

        if len(CurList) <= 2:
            print("YES")
        else:
            print("NO")