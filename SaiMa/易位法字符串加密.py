if __name__ == '__main__':
    que = input()  # DCAB
    strList = list(input().split(" "))  # ["I", "love", "China"]
    newStr = ""
    for letter in strList:
        newStr += letter
    newStr = newStr.upper()

    dic = {}
    for i in range(len(que)):
        dic[que[i]] = []  # {"D":[], "C":[], "A":[], "B":[]}

    strLen = len(newStr)
    dicLen = len(dic)

    for i in range(dicLen - (strLen % dicLen)):  # 先补E
        newStr += "E"

    strLen = len(newStr)
    index = 0

    while index < strLen:
        dic[que[0]].append(newStr[index])
        index += 1
        dic[que[1]].append(newStr[index])
        index += 1
        dic[que[2]].append(newStr[index])
        index += 1
        dic[que[3]].append(newStr[index])
        index += 1

    resStr = ""
    keySort = sorted(dic)
    for key in keySort:
        for _ in dic[key]:
            resStr += _

    print(resStr)
