t = int(input())
paper = [[0]*101 for _ in range(101)]
cnt = 0

for _ in range(t):
    x, y = map(int, input().split())
    for yi in range(10):
        for xi in range(10):
            paper[y+yi][x+xi] = 1

for i in paper:
    cnt += sum(i)
print(cnt)
