x = []
y = []

for i in range(3):
    xx, yy = map(int, input().split())
    x.append(xx)
    y.append(yy)
print([i for i in x if x.count(i)==1][0], [i for i in y if y.count(i)==1][0])