n = int(input())
lst = list(map(int, input().split()))
m = max(lst)
lstt = [x/m * 100 for x in lst]
print(sum(lstt)/n)    