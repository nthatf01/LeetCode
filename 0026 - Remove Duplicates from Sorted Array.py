import time
import sys

startTime = time.perf_counter()


class Solution(object):
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = []
        
        k = 0
        
        for num in nums:
            if num not in nums_set:
                nums_set.append(num)
                nums[k] = num
                k += 1

        return k
    
sol = Solution

nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]
nums3 = [1]
nums4 = [1,2]
nums5 = [-1,0,0,0,0,3,3]

print(f"k = {sol.removeDuplicates(nums1)}, nums = {nums1}")
print(nums1)
print(f"k = {sol.removeDuplicates(nums2)}, nums = {nums2}")
print(nums2)
print(f"k = {sol.removeDuplicates(nums3)}, nums = {nums3}")
print(nums3)
print(f"k = {sol.removeDuplicates(nums4)}, nums = {nums4}")
print(nums4)
print(f"k = {sol.removeDuplicates(nums5)}, nums = {nums5}")
print(nums5)




print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)





