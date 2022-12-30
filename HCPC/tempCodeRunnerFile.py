case = int(input())
top = input().split()
top = [int(i) for i in top]
bottom = input().split()
bottom = [int(i) for i in bottom]
height = []

for i in range(case):
    height.append(top[i] - bottom[i])

bird = int(input())
size = input().split()
w = [int(i) for i in size]

for i in w:
    temp = i
    score = 0
    while True:
        if score == case:
            print(score)
            break
        elif temp <= height[score]:
            score += 1
        else:
            print(score)
            break