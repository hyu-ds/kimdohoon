a = int(input())
b = int(input())
_min, _sum = 0, 0

for i in range(a,b+1):
    prime = True
    for j in range(2, round(i**0.5)+1):
        if i%j == 0:
            prime = False
            break
    if i == 1:
        prime = False
    if prime:
        if _min == 0:
            _min = i
        _min = min(_min, i)
        _sum += i

if _min==_sum==0:
    print(-1)
else:
    print(_sum)
    print(_min)