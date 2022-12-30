from itertools import product

def sigma(arr):
    sum_ = 0
    for i in range(5):
        sum_ += arr[i] * (i+1)
    return sum_

def mull(q,m):
    r = 0
    for i in range(5):
        r += q[i] * m[i]
    return r

prob = [0,0,0,0,0]
money = input().split()
money = [int(o) for o in money]
vals = []

for i in product(range(10),range(5),range(3),range(2),range(2)):
    if sigma(i) <= 10:
        vals.append(mull(i,money))

for i in product(range(15),range(7),range(5),range(3),range(3)):
    if sigma(i) <= 15:
        vals.append(mull(i,money))

#print(vals)
print(max(vals))