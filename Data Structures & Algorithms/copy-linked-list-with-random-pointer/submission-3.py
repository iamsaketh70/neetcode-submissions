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
        copyfromold={None:None}
        curr=head
        while curr:
            copy=Node(curr.val)
            copyfromold[curr]=copy

            curr=curr.next
        
        curr=head
        while curr:
            copy=copyfromold.get(curr)
            copy.next=copyfromold.get(curr.next)
            copy.random=copyfromold.get(curr.random)

            curr=curr.next

        
        return copyfromold.get(head,0)





            




        