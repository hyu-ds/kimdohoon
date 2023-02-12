num = int(input())
a = input().split()
a = [int(i) for i in a]
a.sort()

if a[-1] % 2 == 0:
    print(2*a[-1])
else:
    print(a[0] * a[-1])
