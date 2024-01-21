import time
import sys

startTime = time.perf_counter()

class Solution(object):
    def numberOfSteps(num):
        """
        :type num: int
        :rtype: int
        """

        steps = 0

        while num > 0:
            if num % 2 == 1:
                num -= 1
            else:
                num /= 2

            steps += 1

        return steps

sol = Solution
                
case1 = 14
case2 = 8
case3 = 123

print(sol.numberOfSteps(case1))
print(sol.numberOfSteps(case2))
print(sol.numberOfSteps(case3))


print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)





