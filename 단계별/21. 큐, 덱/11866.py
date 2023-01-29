from collections import deque
n, r = map(int, input().split())
queue = deque([i for i in range(1, n+1)])
output = '<'

while queue:
    queue.rotate(1-r)
    output += f'{queue.popleft()}, '
print(output[:-2] + '>')