from fractions import Fraction

_ = int(input())
r = list(map(int, input().split()))

for i in r[1:]:
    if r[0] % i == 0:
        print(f'{int(r[0]/i)}/1')
    else:
        print(Fraction(r[0], i))