n = int(input())
n_int = input().split()
m = int(input())
m_int = input().split()
ans = ""

for i in range(m):
    ans += f'{int(m_int[i] in n_int)} '
print(ans[:-1])