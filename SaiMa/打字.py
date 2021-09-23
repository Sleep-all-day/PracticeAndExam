def hitword():
    num = int(input())
    for _ in range(num):
        res = 0
        str = input()
        Len = len(str)
        flag = True  # 小写标识符
        for i in range(Len - 1):
            if flag:  # 小写状态下
                if str[i] >= 'a' and str[i] <= 'z':  # 首字母小写
                    res += 1
                else:  # 首字母大写
                    if str[i + 1] >= 'a' and str[i + 1] <= 'z':  # 第二个字母小写
                        res += 2
                    else:  # 第二个字母还是大写
                        res += 2
                        flag = False
            else:  # 大写状态下
                if str[i] >= 'A' and str[i] <= 'Z':  # 首字母大写
                    res += 1
                else:  # 首字母小写
                    if str[i + 1] >= 'A' and str[i + 1] <= 'Z':  # 第二个字母大写
                        res += 2
                    else:  # 第二个字母还是小写
                        res += 2
                        flag = True
        if (flag and str[Len - 1] >= 'a' and str[Len - 1] <= 'z') or (
                flag == False and str[Len - 1] >= 'A' and str[Len - 1] <= 'Z'):
            res += 1
        else:
            res += 2
        print(res)


if __name__ == '__main__':
    num = int(input())
    for _ in range(num):
        res = 0
        str = input()
        Len = len(str)
        flag = True  # 小写标识符
        for i in range(Len - 1):
            if flag:  # 小写状态下
                if str[i] >= 'a' and str[i] <= 'z':  # 首字母小写
                    res += 1
                else:  # 首字母大写
                    if str[i + 1] >= 'a' and str[i + 1] <= 'z':  # 第二个字母小写
                        res += 2
                    else:  # 第二个字母还是大写
                        res += 2
                        flag = False
            else:  # 大写状态下
                if str[i] >= 'A' and str[i] <= 'Z':  # 首字母大写
                    res += 1
                else:  # 首字母小写
                    if str[i + 1] >= 'A' and str[i + 1] <= 'Z':  # 第二个字母大写
                        res += 2
                    else:  # 第二个字母还是小写
                        res += 2
                        flag = True
        if (flag and str[Len - 1] >= 'a' and str[Len - 1] <= 'z') or (
                flag == False and str[Len - 1] >= 'A' and str[Len - 1] <= 'Z'):
            res += 1
        else:
            res += 2
        print(res)
