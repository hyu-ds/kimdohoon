num = int(input())
people = []
ans = ""

for i in range(num):
    p, q = map(int, input().split())
    people.append([p,q])

for i in people:
    rank = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    ans += f"{rank} "

print(ans[:-1])