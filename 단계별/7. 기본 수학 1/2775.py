from functools import cache

@cache
def living(floor, ho):
    r = 0
    if floor == 0:
        r = ho
    else:
        for h in range(1,ho+1):
            r += living(floor-1, h)
    return r

t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    print(living(k, n))