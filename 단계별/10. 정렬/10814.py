import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    age, name = input().split()
    lst.append((int(age), name))
lst.sort(key=lambda x: x[0])
for i in lst:
    print(*i)