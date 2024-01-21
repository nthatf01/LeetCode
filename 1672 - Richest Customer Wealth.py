class Solution(object):
    def maximumWealth(accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxW = 0
        for i in range(0, len(accounts)):
            maxW = max(maxW, sum(accounts[i]))

        return maxW

sol = Solution

case1 = [[1,2,3],[3,2,1]]
case2 = [[1,5],[7,3],[3,5]]
case3 = [[2,8,7],[7,1,3],[1,9,5]]

print(sol.maximumWealth(case1))
print(sol.maximumWealth(case2))
print(sol.maximumWealth(case3))
