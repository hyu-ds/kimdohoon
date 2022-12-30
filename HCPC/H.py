case = int(input())
top = input().split()
top = [int(i) for i in top]
bottom = input().split()
bottom = [int(i) for i in bottom]
height = []

for i in range(case):
    height.append(abs(top[i] - bottom[i]))

bird = int(input())
size = input().split()
w = [int(i) for i in size]

for i in range(bird):
    temp = w[i]
    score = 0
    while score < case:
        if temp <= height[score]:
            score += 1
        else:
            break
    print(score)