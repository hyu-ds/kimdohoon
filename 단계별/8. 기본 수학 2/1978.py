t = int(input())
nums = list(map(int, input().split()))
s = 0

for i in range(t):
    temp = nums[i]
    prime = True
    if temp == 1:
      pass
    else:
      for j in range(2, round(temp**0.5)+1):
          if temp%j == 0:
              prime = False
              break
      if prime:
          s+=1
print(s)