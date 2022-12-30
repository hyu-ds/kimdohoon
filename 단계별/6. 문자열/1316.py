t = int(input())
s = 0
for i in range(t):
    ss = input()
    ss += "$"
    banned = []
    for j in range(1,len(ss)):
        if ss[j] != ss[j-1]:
            if ss[j-1] not in banned:
                banned.append(ss[j-1])
            else:
                s -= 1
                break
    s += 1

print(s)