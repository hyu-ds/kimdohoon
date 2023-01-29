import sys
input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))

t = int(input())
for _ in range(t):
    i,j,k = map(int, input().split())
    cnt = 0
    for e in range(i-1, j):
        cnt += int(sequence[e] > k)
    print(cnt)