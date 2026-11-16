# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        data = []
    
        head = list1
        while head:
            data.append(head.val)
            head = head.next
        
        head = list2
        while head:
            data.append(head.val)
            head = head.next
        head = ListNode(0)
        res = head
        data = sorted(data)
        for ele in data:
            curr_node = ListNode(ele)
            head.next = curr_node
            head = head.next
        res = res.next
        return res
