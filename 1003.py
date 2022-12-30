def fibonacci(n):
    return (((1+5**0.5)/2)**n-((1-5**0.5)/2)**n) * (5**(-0.5))

cycle = int(input())
for i in range(cycle):
    num = int(input())
    if num == 0:
        print("1 0")
    else:
        print(int(fibonacci(num-1)), int(fibonacci(num)))