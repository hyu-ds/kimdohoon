n = int(input())
case_ = 2**(n // 2) * (n // 2 + 1) * (2 - n % 2)  - (1 - n % 2)
print(case_ % 10007)