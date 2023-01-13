def turn2(lst_):
    lst_.append(lst_.pop(0))
    return lst_

def turn3(lst_):
    temp = lst_.pop()
    lst_ = [temp] + lst_
    return lst_

N, M = map(int, input().split())
lst = [0] * (N + 1)
ind = input().split()
for i in ind:
    lst[int(i)] += 1

