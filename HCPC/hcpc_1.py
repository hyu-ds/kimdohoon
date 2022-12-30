# F
times = int(input())
lst = {}
ss = ""
for _ in range(times):
    a, b, c = input().split()
    lst[int(b)] = [a,int(c)]

for p in sorted(lst.keys()):
    ind = lst[p][1]-1
    ss += lst[p][0][ind].upper()

print(ss)