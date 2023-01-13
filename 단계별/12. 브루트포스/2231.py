n = int(input())
generator = -1
for i in range(n):
    s = 0
    gen = i
    while gen > 0:
        s += gen % 10
        gen = gen // 10
    if s + i == n:
        generator = i
        break

print(generator)