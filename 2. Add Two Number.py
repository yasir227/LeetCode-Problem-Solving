class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy head to simplify result list creation
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        # Traverse both lists until both are exhausted
        while l1 or l2 or carry:
            # Get values from current nodes or 0 if None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10

            # Append new node to result list
            current.next = ListNode(new_val)
            current = current.next

            # Move to next nodes if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next