# Longest Common Prefix
lst = []
commlst = []
print("Enter 3 strings: ")
try:
    for _ in range(3):
        ipt = input()
        lst.append(ipt)
    print(lst)
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == lst[i+1][j] == lst[i+2][j]:
                print(lst[i][j], end="")
except IndexError:
    pass
