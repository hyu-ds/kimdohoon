test_case = int(input())

for i in range(test_case):
    a, b = input().split()
    a, b = int(a), int(b)
    mul = a
    list = []
    while True:
        if a%10 not in list:
            list.append(a%10)
            a = a * mul
        else:
            break
    if mul%10 == 0:
        print("10")
    else:
        index = b % len(list)
        print(list[index-1])
