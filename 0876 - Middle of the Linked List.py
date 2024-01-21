import time
import sys
import math

startTime = time.perf_counter()

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        medNode = 0

        current = head

        while current is not None:
            medNode += 1
            current = current.next

        medNode = int(math.floor(medNode / 2))
        current = head

        for i in range(0, medNode):
            current = current.next

        return current


            

        
    

sol = Solution
                
case1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode (5)))))
case2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode (5, ListNode(6))))))

print(sol.middleNode(case1))
print(sol.middleNode(case2))


print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)





