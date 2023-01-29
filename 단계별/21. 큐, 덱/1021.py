from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ind = input().split()
deq = [0 for _ in range(n)]
order = 1
for i in ind:
    deq[int(i)-1] = order
    order += 1
deq = deque(deq)
order = 1
cnt = 0

while order <= m:
    temp = deq.index(order)
    if temp == 0:
        pass
    elif temp <= len(deq) / 2:
        while deq[0] != order:
            deq.rotate(-1)
            cnt += 1
    else:
        while deq[0] != order:
            deq.rotate(1)
            cnt += 1
    deq.popleft()
    order += 1
print(cnt)