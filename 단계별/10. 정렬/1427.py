tarnum = input()
lst = []
for i in tarnum:
    lst.append(int(i))
lst.sort()
for i in lst[::-1]:
    print(i, end="")
print()