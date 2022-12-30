def cache(fn): 
    fn._cache = {}
    def modified_fn(*args):
        if args not in fn._cache:
            fn._cache[args] = fn(*args)
        return fn._cache[args]
    return modified_fn

@cache
def prime(number):
    tf = True
    for i in range(2, int(number**0.5)+1):
        if number%i == 0:  
            tf = False
            break
    return tf

while True:
    n = int(input())
    num = 0
    if n == 0: break
    for i in range(n+1, 2*n+1):
        if prime(i) and i != 1: num += 1
    print(num)
