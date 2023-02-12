n, m = map(int, input().split())

choiso = 0
choidae = []
for i in range(min(n, m)):
    if n % (i+1) == 0 and m % (i+1) == 0:
        choidae.append(i+1)

choidae = max(choidae)
choiso = n * (m / choidae)

print(choidae)
print(int(choiso))
