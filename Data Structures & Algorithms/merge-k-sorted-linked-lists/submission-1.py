# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self,node):
        self.node=node
    def __lt__(self,other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        res=ListNode(0)
        curr=res
        minheap=[]
        for ls in lists:
            if ls is not None:
                heapq.heappush(minheap,NodeWrapper(ls))

        while minheap:
            nodewrapper=heapq.heappop(minheap)
            curr.next=nodewrapper.node
            curr=curr.next

            if (nodewrapper.node.next):
                heapq.heappush(minheap,NodeWrapper(nodewrapper.node.next))

        return res.next

        