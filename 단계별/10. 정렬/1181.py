import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    temp = input().strip('\n')
    if temp not in lst:
        lst.append(temp)
lst.sort(key=lambda x: (len(x),x))
for i in lst:
    print(i)