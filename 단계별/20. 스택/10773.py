import sys
input = sys.stdin.readline
t = int(input())

stack = []
for _ in range(t):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
print(sum(stack))