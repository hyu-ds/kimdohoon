import sys, collections
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
print(round(sum(lst)/len(lst)))

lst.sort()
print(lst[len(lst) // 2])

freq = collections.Counter(lst).most_common()
if len(freq) > 1:
    if freq[0][1] == freq[1][1]:
        print(freq[1][0])
    else:
        print(freq[0][0])
else:
    print(freq[0][0])

print(max(lst)-min(lst))

# 평균 중위값 최빈값 범위