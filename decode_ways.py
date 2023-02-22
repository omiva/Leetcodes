import re


def decode_ways(s):
    d = {}
    decode_count = 0
    count = 0
    j = 1
    for i in range(97, 123):
        d[str(j)] = chr(i)
        j += 1
    print(d)
    if s in d.keys():
        decode_count += 1
        print("d_count1:",decode_count)
        print(s, d[s])
    s_list = list(s)
    for i in range(len(s_list)):
        if s[i] in d.keys():
            count += 1
            if count == len(s_list) and len(s_list) != 1:
                decode_count += 1
                print("d_count2:", decode_count)
            print(decode_count, d[s[i]])
        else:
            continue
    s_rev = ''.join(s_list[::-1])
    print(s_list)
    print(s_rev)
    if len(s_list) > 2:
        if str(int((int(s) / 100))) and str((int(s) % 100)) in d.keys():
            decode_count += 1
            print(str(int((int(s) / 100))), str((int(s) % 100)))
            print("d_count3:", decode_count)
        if str(int(int(s_rev) / 100)) and str(int(s_rev) % 100) in d.keys():
            print(str(int(int(s_rev) / 100)), str(int(s_rev) % 100))
            print("d_count4:", decode_count)
            decode_count += 1
    print(decode_count)


decode_ways(input())
