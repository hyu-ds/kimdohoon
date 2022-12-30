t = int(input())
queue = []
output = []
for i in range(t):
    cmd = input().split()
    if cmd[0] == "push":
        queue.append(int(cmd[1]))
    if cmd[0] == "pop":
        output.append(queue.pop(0) if len(queue)>=1 else -1)
    if cmd[0] == "size":
        output.append(len(queue))
    if cmd[0] == "empty":
        output.append(int(not bool(len(queue))))
    if cmd[0] == "front":
        output.append(queue[0] if len(queue)>=1 else -1)
    if cmd[0] == "back":
        output.append(queue[-1] if len(queue)>=1 else -1)
for i in output:
    print(i)