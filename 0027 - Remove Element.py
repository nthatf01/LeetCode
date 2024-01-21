import time
import sys

startTime = time.perf_counter()


class Solution(object):
    def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left_pointer = 0
        right_pointer = len(nums) - 1

        return_count = len(nums) - nums.count(val)

        if len(set(nums)) == 1 and nums[0] == val:
            return 0

        if val not in nums:
            return len(nums)

        while right_pointer > left_pointer:
            if nums[left_pointer] == val:
                nums[left_pointer] = nums[right_pointer]
                nums[right_pointer] = 0
                right_pointer -= 1
            else:
                left_pointer += 1
                
        return return_count

sol = Solution

nums1 = [3,2,2,3]
val1 = 3
nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
nums3 = [3,3]
val3 = 3
nums4 = [4,5]
val4 = 5
nums5 = [0,1,2,2,3,0,4,2]
val5 = 2
nums6 = [2]
val6 = 3
nums7 = [2,2,3]
val7 = 2

print(f"k = {sol.removeElement(nums1, val1)}, nums = {nums1}")
print(f"k = {sol.removeElement(nums2, val2)}, nums = {nums2}")
print(f"k = {sol.removeElement(nums3, val3)}, nums = {nums3}")
print(f"k = {sol.removeElement(nums4, val4)}, nums = {nums4}")
print(f"k = {sol.removeElement(nums5, val5)}, nums = {nums5}")
print(f"k = {sol.removeElement(nums6, val6)}, nums = {nums6}")
print(f"k = {sol.removeElement(nums7, val7)}, nums = {nums7}")




print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)





