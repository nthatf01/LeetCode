
nums = [-4, -1, 0, 3, 10]
for i in range (0, len(nums)):
    print(f"nums[i] before: {nums[i]}")
    nums[i] = nums[i] ** 2
    print(f"nums[i] after: {nums[i]}")

nums.sort()
        
print(nums)
