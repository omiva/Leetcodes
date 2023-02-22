# import random
# eq = input("equation = ").split()
# i = 0
# print(eq,'\n\n')
# eq1 = []
# eq2 = []
# for i in range(len(eq)):
#     if "==" in eq[i]:
#         for j in range(len(eq[i])):
#             if {eq[i][0], eq[i][3]} not in eq1:
#                 eq1.append({eq[i][0], eq[i][3]})
#
#     if "!" in eq[i]:
#         for j in range(len(eq[i])):
#             if {eq[i][0], eq[i][3]} not in eq2:
#                 eq2.append({eq[i][0], eq[i][3]})
#
#
# for i in range(len(eq1)-1):
#     for j in eq1[i]:
#         if j in eq1[i+1]:
#             new_set = eq1[i].union(eq1[i+1])
#             new_set.remove(j)
#             eq1.append(new_set)
#
# print("eq1 = ",eq1)
# print("eq2 = ", eq2)
# for i in eq2:
#     if i in eq1:
#         print('false')
#     else:
#         print('true')
#
#


def equationsPossible():
    eq = ["a==b","e==c","b==c","a!=e"]

    eq1 = []
    eq2 = []
    for i in range(len(eq)):
        if "==" in eq[i]:
            for j in range(len(eq[i])):
                if eq[i][0] == eq[i][3]:
                    continue
                if {eq[i][0], eq[i][3]} not in eq1:
                    eq1.append({eq[i][0], eq[i][3]})
        if "!" in eq[i]:
            for j in range(len(eq[i])):
                if eq[i][0] == eq[i][3]:
                    continue
                if {eq[i][0], eq[i][3]} not in eq2:
                    eq2.append({eq[i][0], eq[i][3]})

    for i in range(len(eq1) - 1):
        for j in eq1[i]:
            if j in eq1[i + 1]:
                new_set = eq1[i].union(eq1[i + 1])
                new_set.remove(j)
                eq1.append(new_set)

    for i in range(len(eq2) - 1):
        for j in eq2[i]:
            if j in eq2[i + 1]:
                new_set = eq2[i].union(eq2[i + 1])
                new_set.remove(j)
                eq2.append(new_set)
    print(eq1)
    print(eq2)
    if len(eq2) == 0:
        return True
    if len(eq1) == 0:
        return False
    for i in eq2:
        if i in eq1:
            return False
        else:
            return True

print(equationsPossible())