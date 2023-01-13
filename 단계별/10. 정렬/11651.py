import sys
input = sys.stdin.readline
lst = []
for i in range(int(input())):
    a, b = map(int, input().split())
    lst.append((a,b))
lst.sort(key=lambda x: (x[1], x[0]))
for i in lst:
    print(*i)