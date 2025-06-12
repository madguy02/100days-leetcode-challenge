
# Problem: https://leetcode.com/problems/add-two-numbers/description/

from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        carry = 0
        curr = dummy

        while l1 or l2 or carry:
            sum = carry

            if l1:
                sum += l1.val
                l1 = l1.next
            
            if l2:
                sum += l2.val
                l2 = l2.next
        
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
        
        return dummy.next