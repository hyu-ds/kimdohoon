while True:
    nums = [int(i) for i in input().split()]
    if nums.count(0) == 3: break
    else:
        bit = max(nums)
        nums.remove(bit)
        if bit**2 == nums[0]**2 + nums[1]**2:
            print('right')
        else:
            print('wrong')