import sys
input = sys.stdin.readline

sentences = []
while True:
    temp = input().strip('\n')
    if temp == '.':
        break
    else:
        sentences.append(temp)

for s in sentences:
    stack = []
    for char in s:
        if char in "()[]":
            if char in "([" or len(stack) == 0:
                stack.append(char)
            elif char == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(char)
            elif char == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(char)
    if len(stack) == 0:
        print('yes')
    else:
        print('no')