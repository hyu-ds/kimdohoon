import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    num, where = map(int, input().split())
    docs = deque(map(int, input().split()))
    target = deque([False for _ in range(num)])
    target[where] = True
    order = 1

    while True:
        if docs[0] == max(docs):
            if target[0]:
                print(order)
                break
            else:
                docs.popleft()
                target.popleft()
                order += 1
        else:
            docs.rotate(-1)
            target.rotate(-1)