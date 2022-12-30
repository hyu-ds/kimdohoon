t = int(input())
for i in range(t):
    s = input()
    score = 0
    adding = 1
    for j in s:
        if j == "O":
            score += adding
            adding += 1
        else:
            adding = 1
    print(score)

