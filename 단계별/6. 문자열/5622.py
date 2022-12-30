alph = "abc def ghi jlk mno pqrs tuv wxyz".split()
ss = input().lower()
_sum = 0

for i in ss:
    for ap in alph:
        if i in ap:
            ind = alph.index(ap)+3
            break
    _sum += ind
print(_sum)