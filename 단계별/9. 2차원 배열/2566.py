M = []
m = []
for i in range(9):
    nums = [int(i) for i in input().split()]
    m.append(max(nums))
    M.append(nums)
max_value = max(m)
print(max_value)
print(m.index(max_value)+1, M[m.index(max_value)].index(max_value)+1)