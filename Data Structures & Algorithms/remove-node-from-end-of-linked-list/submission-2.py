# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
         
        # temp = head
        # count = 0
        # while temp:
        #     count += 1
        #     temp = temp.next
        # index_remove = count - n
        # i = 0
        # res = head
        # prev = head
        # if index_remove == 0:
        #     return head.next
        # while i < index_remove:
        #     prev = head
        #     head = head.next
        #     i += 1
        # prev.next = head.next
        # return res
        dummy = ListNode(0)
        dummy.next = head

        fast = slow = dummy
        

        for _ in range(n+1):
            fast = fast.next
        
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        
        # Now slow pointer is at edge where to cut and present the linkedlist 
        
        slow.next = slow.next.next       
        return dummy.next
        