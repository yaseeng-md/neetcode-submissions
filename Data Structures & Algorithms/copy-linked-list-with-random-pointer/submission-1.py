"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCurr = {None : None}

        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCurr[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = oldToCurr[curr]
            copy.next = oldToCurr[curr.next]
            copy.random = oldToCurr[curr.random]
            curr = curr.next
        
        return oldToCurr[head]
        