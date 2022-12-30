test_case = int(input())

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

for i in range(test_case):
    r, n = input().split()
    r, n = int(r), int(n)
    comb = fact(n)/(fact(r) * fact(n-r))
    print(int(comb))
    

