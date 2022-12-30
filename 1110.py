def cycle(n_):
    cal = n_ // 10 + n_ % 10
    t_ = int(str(n_%10) + str(cal%10))
    return t_

num = int(input())
t = num
cn = 1
while num != cycle(t):
    cn += 1
    t = cycle(t)
print(cn)