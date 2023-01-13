import sys, queue
input = sys.stdin.readline

t = int(input())
queue = queue.Queue()

for _ in range(t):
    cmd = input().split()
    if cmd[0] == 'push':
        queue.put(int(cmd[1]))
    if cmd[0] == 'pop':
        print(queue.get())
    if cmd[0] == 'size':
        print(queue.qsize())
    if cmd[0] == 'empty':
        print(int(queue.empty()))
    if cmd[0] == 'front':
        if queue.empty():
            print(-1)
        else:
            print(queue[0])
    if cmd[0] == 'back':
        if queue.empty():
            print(-1)
        else:
            print(queue[-1])