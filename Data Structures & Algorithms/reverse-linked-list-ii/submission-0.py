# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy=ListNode(0,head)
        before=dummy

        for i in range(left-1):
            before=before.next

        start=before.next
        cur=start
        prev=None

        for i in range(right-left+1):
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt

        before.next=prev
        start.next=cur

        return dummy.next


        

            

        

            


                

                