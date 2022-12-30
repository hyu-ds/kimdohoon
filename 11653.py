n = int(input())
def cache(fn): 
    fn._cache = {}
    def modified_fn(*args):
        if args not in fn._cache:
            fn._cache[args] = fn(*args)
        return fn._cache[args]
    return modified_fn

@cache
def prime_num(k):
    primes = [True] * (k+1)
    for i in range(2, int(k**0.5)+1):
        if primes[i]:
            for j in range(2*i,k,i):
                primes[j] = False
    return [i for i in range(2, k+1) if primes[i] == True]

if n != 1:
    div_num = prime_num(n)

while(n != 1):
    for i in div_num:
        if n % i == 0:
            print(i)
            n = n / i
            break

