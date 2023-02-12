def factorial(n):
    fact_result = 1
    for i in range (n,1,-1):
        fact_result = fact_result * i
    return fact_result

n, k = input().split(" ")
n = int(n)
k = int(k)
print(int(factorial(n)/(factorial(k)*factorial(n-k))))