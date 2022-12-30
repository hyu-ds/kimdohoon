n, m = map(int, input().split())
arr1 = [[*map(int, input().split())] for _ in range(n)]
arr2 = [[*map(int, input().split())] for _ in range(n)]

rvalue = []
for r1, r2 in zip(arr1, arr2):
    for i in range(m):
        temp = [a+b for a in r1 for b in r2]
        rvalue.append()