import sys
input = sys.stdin.readline
n = int(input())
seq = []
for _ in range(n):
    seq.append(int(input()))

num = 1
stack = []
output = []
for num in range(1, n+1):
    stack.append(num)
    output.append('+')
    while True:
        if len(seq) == 0:
            break
        else:
            try:
                if stack[-1] != seq[0]:
                    break
                else:
                    stack.pop()
                    del seq[0]
                    output.append('-')
            except:
                break

if len(seq) == 0:
    for i in output:
        print(i)
else:
    print("NO")