def canConstruct(ransomNote, magazine):
    flag = 0
    checklist1 = {}
    checklist2 = {}
    for i in list(ransomNote):
        if i not in checklist1:
            checklist1[i] = 1
        else:
            checklist1[i] += 1

    for i in list(magazine):
        if i not in checklist2:
            checklist2[i] = 1
        else:
            checklist2[i] += 1
    print(checklist1)
    print(checklist2)

    for i, j in checklist1.items():
        # print('\n'+i,j)
        if i in checklist2 and checklist2[i] >= j:
            flag = 1
        else:
            flag = 0
            return flag


print(canConstruct("chejaccdae", "geceeibccchjejhdd"))
