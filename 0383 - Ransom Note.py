import time
import sys

startTime = time.perf_counter()

class Solution(object):
    def canConstruct(ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magDict = {}

        for char in magazine:
            if char not in magDict:
                magDict[char] = 1
            else:
                magDict[char] += 1

        for char in ransomNote:
            if char not in magDict:
                return False
            else:
                magDict[char] -= 1
                if magDict[char] == 0:
                    del magDict[char]
        
        return True


        
    

sol = Solution
                
case1 = ("a", "b")
case2 = ("aa", "ab")
case3 = ("aa", "aab")

print(sol.canConstruct(*case1))
print(sol.canConstruct(*case2))
print(sol.canConstruct(*case3))



print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)





