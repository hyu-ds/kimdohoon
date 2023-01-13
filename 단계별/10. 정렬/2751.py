import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    k = int(input())
    lst.append(k)
lst.sort()
for i in lst:
    print(i)