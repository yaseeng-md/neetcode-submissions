# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if  head or  head.next:
            
            
            # STEP 1: Find middle
            slow = head
            fast = head

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            # STEP 2: Split the linked list
            second = slow.next
            slow.next = None

            # STEP 3: Reverse second half
            prev = None
            curr = second

            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            second = prev

            # STEP 4: Merge both halves
            first = head

            while second:
                first_next = first.next
                second_next = second.next

                first.next = second
                second.next = first_next

                first = first_next
                second = second_next

            # return head