import time
import sys

startTime = time.perf_counter()

class Solution(object):
    def replaceElements(arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        right_max = 0

        for i, e in reversed(list(enumerate(arr))):
            if arr[i] > right_max:
                arr[i], right_max = right_max, arr[i]
            else:
                arr[i] = right_max

        arr[-1] = -1

        return arr
                
sol = Solution
                
case1 = [17,18,5,4,6,1]
case2 = [400]
case3 = [1,0,2,3,0,4,5,0]

print(sol.replaceElements(case1))
print(sol.replaceElements(case2))
print(sol.replaceElements(case3))



print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)





