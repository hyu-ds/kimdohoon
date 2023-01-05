n, m = map(int, input().split())
A = []
B = []
for i in range(n):
    nums = [int(j) for j in input().split()]
    A.append(nums)
for i in range(n):
    nums = [int(j) for j in input().split()]
    B.append(nums)

for i in range(n):
    for j in range(m):
        print(A[i][j]+B[i][j], end=" ")
    print()