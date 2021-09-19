num = int(input())
_dict = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


for _ in range(num):
    letter_len = int(input())
    letter = input()
    time = 1
    res = ""
    for i in range(letter_len - 1):
        if letter[i] == letter[i + 1]: # 下一个相同
            if letter[i + 1] in _dict.keys(): #是字母
                time += 1
            elif letter[i + 1] == "0":
                res += "-"
                time = 1
            elif letter[i + 1] == "-":
                time = 1

        else: # 下一个不同
            if letter[i] in _dict.keys(): #第一个是字母
                if letter[i + 1] != "-":#非延时直接结算
                    if letter[i + 1] == "0":
                        res += _dict[letter[i]][time]
                        res += "-"
                        time = 1
                    else: # 字母
                        res += _dict[letter[i]][time]
                        time = 1
                else:
                    if letter
            elif letter[i] == "0": #是0，直接处理
                res += _dict[letter[i]][time]
    if time != 0:#最后结算
