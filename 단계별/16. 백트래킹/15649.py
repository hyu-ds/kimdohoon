from itertools import permutations

n, m = map(int, input().split())
lst = [i+1 for i in range(n)]
for i in permutations(lst, m):
    print(*i)