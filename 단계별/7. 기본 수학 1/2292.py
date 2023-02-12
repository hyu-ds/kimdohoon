n = int(input())
cnt = 1
bee = 1

while bee < n:
    bee += 6 * cnt
    cnt += 1
print(cnt)