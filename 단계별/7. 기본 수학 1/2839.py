def numm(n5, n3):
    return 5 * n5 + 3 * n3

n = int(input())
st = n // 5 + 1
stop = False

while not stop:
    if st != 0:
        for i in range(st+1):
            if numm(i, st - i) == n:
                stop = True
                print(st)
                break
    else:
        if n % 3 == 0:
            print(n//3)
            stop = True
        else:
            print(-1)
            stop = True
    st -= 1