def maxSubArray(nums) -> int:
    cur_i = 0
    res = 0
    while cur_i < len(nums) - 1:
        if nums[cur_i] * nums[cur_i+1] >=0:
            nums[cur_i] += nums[cur_i+1]
            del nums[cur_i+1]
            cur_i -= 1
        cur_i += 1
    print(nums)
    cur_i = 0 

    if nums[0] < 0:
        del nums[0]

    while 1 < cur_i < len(nums) - 1:
        if nums[cur_i] >= 0:
            if nums[cur_i - 1] > nums[cur_i + 1]:
                nums[cur_i] += nums[cur_i - 1]
                del nums[cur_i - 1]
            else:
                nums[cur_i] += nums[cur_i + 1]
                del nums[cur_i + 1]
        cur_i += 1 
    print(nums)


maxSubArray([-2, 2, 8, 1,-3,4,-1,2,-1, 8,1,-5,-1])