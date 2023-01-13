import sys
input = sys.stdin.readline

_ = input()
nums = list(map(int, input().split()))
numss = sorted(nums)
dict_ = {}
ind = 0
for i in numss:
    if i not in dict_.keys():
        dict_[i] = ind
        ind += 1
for i in nums:
    print(dict_[i], end=" ")
print()