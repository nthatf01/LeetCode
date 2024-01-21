import time
import sys

startTime = time.perf_counter()

class Solution(object):
    def checkIfExist(arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        int_list = []

        for i in arr:
            if (i * 2) in int_list:
                return True
            elif i % 2 == 0 and i / 2 in int_list:
                return True
            else:
                int_list.append(i)

        return False
              
sol = Solution
                
case1 = [10,2,5,3]
case2 = [3,1,7,11]
case3 = [0,0]

print(sol.checkIfExist(case1))
print(sol.checkIfExist(case2))
print(sol.checkIfExist(case3))



print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)





