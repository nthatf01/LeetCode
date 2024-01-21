import time
import sys

startTime = time.perf_counter()

class Solution(object):
    def duplicateZeros(arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        j = 0
        nextArg = 0
        while i < len(arr):
            if arr[i] == 0:
                j = i + 1
                currArg = arr[i]
                while j < len(arr):
                    nextArg = arr[j]
                    arr[j] = currArg
                    currArg = nextArg
                    j += 1
                i += 2
            else:
                i += 1

                
sol = Solution
                
case1 = [1,0,2,3,0,4,5,0]
case2 = [1,0,2,3,0,4,5,0]
case3 = [1,0,2,3,0,4,5,0]

print(case1, sol.duplicateZeros(case1), case1)
print(case2, sol.duplicateZeros(case2), case2)
print(case3, sol.duplicateZeros(case3), case3)



print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)





