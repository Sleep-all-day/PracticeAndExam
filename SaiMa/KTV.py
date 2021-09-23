if __name__ == '__main__':
    num = int(input())
    for _ in range(num):  # 每组测试用例
        PeopleNum, MailNum, SongNum = map(int, input().split())
        SongList = []
        for i in range(PeopleNum):  # 记录每个人的歌曲清单
            PersonSong = list(map(int, input().split(" ")))
            for song in range(1, PersonSong[0] + 1):
                SongList.append(PersonSong[song])

        SongList.sort()  # 所有歌曲被记录并排序
        Len = len(SongList)
        count = 0
        songindex = 0
        for songindex in range(Len):
            if songindex == 0:
                SongNum -= 1
            else:
                if SongList[songindex] != SongList[songindex - 1]:
                    SongNum -= 1
                    count = 0
                else:
                    count += 1
                    if count == 3:
                        SongNum -= 1
                        count = 1

        if SongNum < 0:
            print("NO")
        else:
            print("YES")


