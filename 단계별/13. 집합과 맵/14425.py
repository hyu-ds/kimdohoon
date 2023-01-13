import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = ""
check = 0
for _ in range(n):
    s += input()

for _ in range(m):
    if input() in s:
        check += 1
print(check)