# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        curr = head # 1
        fut = head.next if head else None # type: ignore 2
        
        while curr is not None:
            curr.next = prev
            prev = curr
            curr = fut
            
            if fut is not None:
                fut = fut.next
        
        return prev
    