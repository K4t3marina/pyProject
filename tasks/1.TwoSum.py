nums = [3, 20, 75,8 ,86, 3]
target = 6
r = []
for i in range(len(nums)):
    if (target-nums[i]) in nums:
        if nums.index(target-nums[i]) > -1 and nums.index(target-nums[i]) != i:
            r.append(i)
            r.append(nums.index(target-nums[i]))
            break
print(r)