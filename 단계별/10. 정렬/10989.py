import sys
input = sys.stdin.readline
lst = [0] * 10001

for _ in range(int(input())):
    lst[int(input())] += 1

for i in range(len(lst)):
    for _ in range(lst[i]):
        print(i)