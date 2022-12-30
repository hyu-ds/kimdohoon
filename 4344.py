t = int(input())
for i in range(t):
    s = list(map(int, input().split()))
    num = s[0]
    s.remove(s[0])
    ss = [x for x in s if x > sum(s)/num]
    print(f"{round(len(ss) / num * 100, 3):.3f}%")