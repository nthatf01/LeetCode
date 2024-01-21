import time
import sys

startTime = time.perf_counter()

class Solution(object):
    def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left_pointer = 0
        right_pointer = 1

        if len(nums) <= 1:
            return

        while right_pointer < len(nums):
            print(left_pointer)
            if nums[left_pointer] == 0:
                nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
                right_pointer += 1
            else:
                left_pointer += 1

            if right_pointer <= left_pointer:
                right_pointer = left_pointer + 1
                
        return
               
sol = Solution
                
case1 = [0,1,0,3,12]
case2 = [0]
case3 = [1,0,2,3,0,4,5,0]
case4 = [2,1]

print(sol.moveZeroes(case1), case1)
print(sol.moveZeroes(case2), case2)
print(sol.moveZeroes(case3), case3)
print(sol.moveZeroes(case4), case4)



print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)





