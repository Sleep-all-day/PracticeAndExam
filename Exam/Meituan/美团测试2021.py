def solution():
    num = int(input())
    for i in range(num):
        letter = input()
        letterLen = len(letter)
        flag = False
        if letterLen == 0:
            print("YES")
            break
        elif letterLen == 1:
            print("NO")
            break
        else:
            last = letter[0]
            for _ in letter:
                if _ != last:
                    flag = True
                    break
            if flag == True:
                print("YES")
            else:
                print("NO")




if __name__ == '__main__':
    solution()