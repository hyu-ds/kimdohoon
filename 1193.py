def sum_n(n):
    return int(n*(n+1)/2)

def zigzag(_in):
    for i in range(_in+1):
        if _in <= sum_n(i):
            line = i
            break
    temp = _in - sum_n(line-1) - 1
    if line%2 == 0:
        return line + 1 - temp, temp
    else:
        return temp, line - temp + 1

num = int(input())
first,second = zigzag(num)
print(f"{first}/{second}")