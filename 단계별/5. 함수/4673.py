def d(n):
    add = n
    while n//10 != 0:
        add += n%10
        n = n // 10
    return add + n%10

def selfnum(r):
    nums = [True] * r
    for i in range(r):
        if nums[i]:
            that = i+1
            while d(that) <= r:
                nums[d(that)-1] = False
                that = d(that)
    return [i+1 for i in range(r) if nums[i]]

_self = selfnum(10000)
for i in _self:
    print(i)