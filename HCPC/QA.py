#3
N, M = [i for i in map(int, input().split())]
S = [i for i in map(int, input().split())]
for _ in range(M):
    S.append(0)
T = []
for i in range(N):
    k = input().split()
    k = [int(i) for i in k]
    T.append(k)

#Minus
for i in range(N):
    temp = sum(T[i])
    S[i] -= temp

# Plus
for i in range(N):
    for p in range(N):
        S[i] += T[p][i]


for i in range(N, M+N):
    for p in range(N):
        S[i] += T[p][i]

ss = ""
for i in S:
    ss += str(i) + " "
print(ss[:-1])