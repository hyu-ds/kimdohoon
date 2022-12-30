_min, _max = map(int, input().split())
squared_nums = []

for i in range(2, _max+1):
    temp = i
    while True:
        if temp**2 <= _max:
            temp = temp **2
            if temp not in squared_nums:
                squared_nums.append(temp)
        else:
            break

for j in squared_nums:
    for k in range(2,_max):
        if j*k > _max:
            break
        if j*k not in squared_nums:
            squared_nums.append(j*k)
            

squared_nums = [i for i in squared_nums if i>=_min]
#print(sorted(squared_nums))
print(_max - _min + 1 - len(squared_nums))