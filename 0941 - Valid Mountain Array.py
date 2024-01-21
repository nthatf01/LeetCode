import time
import sys

startTime = time.perf_counter()

class Solution(object):
    def validMountainArray(arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        status = "ascending"
        elevation = -1

        if len(arr) < 3:
            return False

        if arr[1] <= arr[0]:
            return False

        for i in arr:
            if i == elevation:
                return False
            
            if status == "ascending":
                if i < elevation:
                    status = "descending"
                elevation = i
            elif status == "descending":
                if i > elevation:
                    return False
                elevation = i
        if status == "ascending":
            return False
        else:
            return True
                     
sol = Solution
                
case1 = [2,1]
case2 = [3,5,5]
case3 = [0,3,2,1]
case4 = [0,1,2,3,4,5,6,7,8,9]

print(sol.validMountainArray(case1))
print(sol.validMountainArray(case2))
print(sol.validMountainArray(case3))
print(sol.validMountainArray(case4))



print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)





