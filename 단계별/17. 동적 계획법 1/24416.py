recursive_call = 0

def recursive_fib(n):
    global recursive_call
    recursive_call += 1
    if n <= 2:
        return 1
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)

def dp_fib(n):
    f = {}
    f[1] = f[2] = 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

num = int(input())
recursive_fib(num)
dp_fib(num)
print(recursive_call, num-2)