# CCW
import sys
input = sys.stdin.readline

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if x1 != x2 and x1 != x3:
    tan1 = (y2 - y1) / (x2 - x1)
    tan2 = (y3 - y1) / (x3 - x1)
    if tan1 == tan2:
        print(0)
    elif tan1 > tan2:
        print(-1)
    else:
        print(1)
elif x1 == x2:
    if x1 == x3:
        print(0)
    elif x1 > x3:
        print(1)
    else:
        print(-1)
elif y1 == y2:
    if y1 == y3:
        print(0)
    elif y1 > y3:
        print(-1)
    else:
        print(1)