def solution():
    str1 = input()
    str2 = input()

    res = ""
    index_list = {}
    for letter in str2:
        if index_list.has_key(letter):
            continue
        else:
            _index = str1.find(letter, 0)
            if _index == -1 :
                print("")
                return 0
            else:
                index_list[letter] = [_index]

                while _index != -1:
                    _index = str1.find(letter, _index)
                    index_list[letter].append(_index)
                    if _index != -1:
                        break

    if len(index_list) == 0:
        res = str1
    else:
        # for key in index_list:
        pass
    print(res)

def getminstr(dict):
    dict_len = len(dict.keys)



if __name__ == "__main__":
    solution()
