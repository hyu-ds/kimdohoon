pos = [0, 0]
vertex = []
chamwoe = int(input())
for i in range(6):
    direction, length = map(int, input().split())
    if direction in [1, 2]:
        pos[0] += length * ((-1)**(direction-1))
    else:
        pos[1] += length * ((-1)**direction)

    vertex.append((pos[0], pos[1]))

vx = [i[0] for i in vertex]
vy = [i[1] for i in vertex]
v = []
for x in [max(vx), min(vx)]:
    for y in [max(vy), min(vy)]:
        v.append((x,y))
not_pass = [i for i in v if i not in vertex][0]
mid = (sorted(vx)[2], sorted(vy)[2])
area = (v[0][0] - v[3][0]) * (v[0][1] - v[3][1]) - abs((not_pass[0] - mid[0]) * (not_pass[1] - mid[1]))
print(area*chamwoe)