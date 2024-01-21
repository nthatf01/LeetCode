class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def createListNode(l3):
            if not l3:
                return None
        
            head = ListNode(int(l3[0]))
            current = head

            for i in range(1, len(l3)):
                current.next = ListNode(int(l3[i]))
                current = current.next

            return head

        #Initialize variables
        str1 = ""
        str2 = ""
        str3 = ""
        num1 = 0
        num2 = 0
        num3 = 0

        #Loop over first linked list and store values in a string
        while l1 is not None:
            str1 += str(l1.val)
            l1 = l1.next

        #Loop over second linked list and store values in a string
        while l2 is not None:
            str2 += str(l2.val)
            l2 = l2.next

        #Reverse the strings
        str1 = str1[::-1]
        str2 = str2[::-1]

        #Convert the strings into integers
        num1 = int(str1)
        num2 = int(str2)

        #Add the two integers
        num3 = num1 + num2

        #Convert the sum into a string and reverse it
        str3 = str(num3)[::-1]

        #Create a linked list from the sum string
        l3 = createListNode(str3)

        return l3

        
               
ln1 = ListNode(2, ListNode(4, ListNode(3)))
ln2 = ListNode(5, ListNode(6, ListNode(4)))

lc2 = Solution

print(lc2.addTwoNumbers(lc2, ln1, ln2))
