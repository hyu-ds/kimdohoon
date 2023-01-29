import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    cmd = input().strip('\n')
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(","))
    error = False
    rev = 0

    if n == 0:
        arr = deque()
    
    for c in cmd:
        if c == "R":
            rev += 1
        elif c == "D":
            if arr:
                if rev % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                error = True
                print('error')
                break
    if not error:
        if rev % 2 == 1:
            arr.reverse()
        print('[' + ','.join(arr) + ']')