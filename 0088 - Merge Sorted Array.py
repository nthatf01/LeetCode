import time
import sys

startTime = time.perf_counter()


class Solution(object):
    def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m > 0:
            for i in range(m, m + n):
                nums1[i] = nums2[i - m]
        else:
            for i in range(0, n):
                nums1[i] = nums2[i]
                
        nums1.sort()





print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)





