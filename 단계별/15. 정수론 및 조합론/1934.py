import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    c = []
    for i in range(min(n, m)):
        if n % (i+1) == 0 and m % (i+1) == 0:
            c.append(i+1)

    c = max(c)

    print(int(n * m / c))