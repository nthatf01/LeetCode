class Solution(object):
    def runningSum(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rSum = []
        for i in range(0, len(nums)):
            rSum.append(sum(nums[0:i+1]))
        return rSum

sol = Solution

case1 = [1, 2, 3, 4]
case2 = [1, 1, 1, 1, 1]
case3 = [3, 1, 2, 10, 1]

print(sol.runningSum(case1))
print(sol.runningSum(case2))
print(sol.runningSum(case3))

