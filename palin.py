#
# def palinCheck(a):
#     b = []
#     for i in a:
#         if i.isalnum():
#             b.append(i)
#         else:
#             continue
#
#     print(''.join(b))
#     print(''.join(b[::-1]))
#     if ''.join(b).lower() == ''.join(b[::-1]).lower():
#         print("palin")
#     else:
#         print("not palin")
#
# palinCheck(input())

a = {1,2,3,4,5}

a.remove(2)
print(a)