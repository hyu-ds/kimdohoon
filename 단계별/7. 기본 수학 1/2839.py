def numm(n5, n3):
    return 5 * n5 + 3 * n3

n = int(input())
st = n // 3 if n % 3 == 0 else n // 5 + 1
stop = False

while not stop:
    if st != 0:
        for i in range(st+1):
            if numm(st - i, i) == n:
                stop = True
                print(st)
                break
    else:
        print(-1)
        stop = True
    st -= 1