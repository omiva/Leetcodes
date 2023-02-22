# def RomToInt(s):
#     # print(s)
#     rev = s[::-1]
#     ans = 0
#     #MCMXCIV
#     cond = ['M'>'D', 'D'>'C', 'C'>'L', 'L'>'X', 'X'>'V', 'V'>'I']
#     for i in s:
#         ans += sym[i]
#     print(ans)
#
#
# sym = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# # sym[0] = 1
# # sym[1] = 5
# # sym[2] = 10
# # sym[3] = 50
# # sym[4] = 100
# # sym[5] = 500
# # sym[6] = 1000
# s = list(input("Enter the roman value: "))
# flag = 0
# for i in s:
#     if i in sym.keys():
#         flag = 1
#     else:
#         flag = 0
#         break
# if flag == 1:
#     RomToInt(s)


# def romanToInt(s):
#     dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90,
#            "CD": 400, "CM": 900}
#     ans = []
#     sums = 0
#     i = 0
#
#     while i < len(s):
#         print(s[i:i + 2])
#         if s[i:i + 2] in dic:
#             print(dic[s[i:i + 2]])
#             sums += dic[s[i:i + 2]]
#             i += 2
#         else:
#             print(dic[s[i]])
#             sums += dic[s[i]]
#             i += 1
#         ans.append(sums)
#     print(ans[-1])
#
#
# s = input('=')
# romanToInt(s)


def RomanToInt(s):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90,
           "CD": 400, "CM": 900}
    sums = 0
    i = 0
    while i < len(s):
        if s[i:i + 2] in dic:
            sums += dic[s[i:i + 2]]
            i += 2
        else:
            sums += dic[s[i]]
            i += 1
    print(sums)


s = input('Enter roman value: ')
RomanToInt(s)
