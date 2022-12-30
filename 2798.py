from itertools import combinations as c

n, m = map(int, input().split())
nums = list(map(int, input().split()))
diff = m
ans = 0

for tpl in c(nums, 3):
    s = tpl[0] + tpl[1] + tpl[2]
    if s <= m and m-s < diff:
        diff = m - s
        ans = s
print(ans)
