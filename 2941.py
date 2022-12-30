croatian = "c= c- dz= d- lj nj s= z=".split()

ss = input()
removed = 0
for cr in croatian:
    while True:
        try:
            ind = ss.index(cr)
            ss = ss[:ind] + "$" + ss[ind+len(cr):]
        except:
            break

print(len(ss))