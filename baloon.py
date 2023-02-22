def baloonBurst(nums):
    a = []
    tot = []
    for i in nums.split():
        a.append(int(i))
    for j in range(len(a)-1):
        try:
            if len(a) >= 3:
                print(1)
                tot.append(a[j] * a[j+1] * a[j+2])
                a.pop(a[j+1])
            elif len(a) < 3:
                print(2)
                if a[j - 1] not in a:
                    a[j - 1] = 1
                tot.append(a[j-1] * a[j] * a[j+1])
        except IndexError:
            if a[j-1] not in a:
                a[j-1] = 1
            print(a[j - 1] * a[j] * a[j + 1])

baloonBurst(input())