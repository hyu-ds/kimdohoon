def hanoi(n, first, second, third):
    if n == 1:
        print(first, third)
    else:
        hanoi(n - 1, first, third, second)
        print(first, third)
        hanoi(n - 1, second, first, third)


num = int(input())
print(2**num - 1)
hanoi(num, 1, 2, 3)