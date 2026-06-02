# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head
        second = head

        while first.next and first.next.next:
            second = second.next
            first = first.next.next

        curr = second.next
        prev = None
        second.next = None
        

        while curr:
            nxt = curr.next
            curr.next = prev
            prev =curr
            curr = nxt
        
        first,second= head,prev
        while second:
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2