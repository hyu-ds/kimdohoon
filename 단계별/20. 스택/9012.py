import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    stack = []
    string = input().strip('\n')
    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                stack.append(i)
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")