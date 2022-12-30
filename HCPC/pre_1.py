def sosu_making(num):
    ss_list = []
    for i in range(2,num+1):
        is_sosu = True
        for j in range(2, i):
            if i % j == 0:
                is_sosu = False
                break
        if is_sosu:
            ss_list.append(i)
    return ss_list

def check_sum(num, lst):
    for i in lst:
        for j in lst:
            if i + j == num:
                return True
    return False

times = int(input())
for i in range(times):
    a = int(input())
    yrn = check_sum(a, sosu_making(a))
    if yrn:
        print("Yes")
    else:
        print("No")