#3
N, M = [i for i in map(int, input().split())]
S = [i for i in map(int, input().split())]
T = []
for i in range(N):
    k=input().split()
    k = [int(i) for i in k]
    T.append(k)

Tminus=0
Tplus=0
total=[]
for i in range(N):
    for j in range(N+M):
        Tminus+=T[i][j]

    t=S[i]-Tminus
    total.append(t)

print(N,M)
print(S)
print(T)
print(T[1][1])