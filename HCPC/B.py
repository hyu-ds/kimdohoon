a, b = map(int, input().split())

lst = []
for _ in range(b):
    c, d = map(int, input().split())
    lst.append([c,d])

num_list = []
num_list2 = []

for i in range (0,b):
    num_list.append(lst[i][0])
    num_list2.append(lst[i][1])

k = True
for i in range(1,a+1):
    if (i not in num_list) or (i not in num_list2) or (a<=b):
        k = False
        break
    
if k:
    print("Yes")
else:
    print("No")