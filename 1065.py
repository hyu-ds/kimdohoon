n = int(input())
count = 0

for i in range(1,n+1):
    temp = i
    if i < 100:
        count += 1
    elif i < 1000:
        a,b,c = temp%10, int(temp/10)%10, int(temp/100)%10
        if b-a == c-b:
            count += 1
print(count)