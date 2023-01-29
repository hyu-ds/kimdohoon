import sys
input = sys.stdin.readline

stack = []
t = int(input())
for _ in range(t):
    cmd = input().split()
    if len(cmd) == 2:
        stack.append(int(cmd[1]))
    else:
        cmd = cmd[0]
        
        if cmd == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif cmd == 'size':
            print(len(stack))
        elif cmd == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif cmd == 'top':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])