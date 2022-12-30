# 1002 터렛 - 두 원의 위치 관계
def length(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

test_num = int(input())
for i in range(test_num):
    list = input().split()
    distance = length(int(list[0]), int(list[1]), int(list[3]), int(list[4]))
    if distance == 0:
        if int(list[2]) == int(list[5]):
            print("-1")
        else:
            print("0")
    elif distance < int(list[2]) + int(list[5]) and distance > abs(int(list[2]) - int(list[5])):
        print("2")
    elif distance == int(list[2]) + int(list[5]) or distance == abs(int(list[2]) - int(list[5])):
        print("1")
    else:
        print("0")

