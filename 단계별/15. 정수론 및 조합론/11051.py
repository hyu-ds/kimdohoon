def factorial(n):
    fact_result = 1
    for i in range (1, n+1):
        fact_result *= i
    return fact_result

n, k = map(int, input().split())
comb = factorial(n) / (factorial(k) * factorial(n-k))
print(int(comb % 10007))