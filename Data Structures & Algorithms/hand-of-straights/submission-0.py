class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count={}
        for n in hand:
            count[n]=1+count.get(n,0)

        minheap=list(count.keys())
        heapq.heapify(minheap)

        while minheap:
            firstnumber=minheap[0]

            for i in range(firstnumber,firstnumber+groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    if i!=minheap[0]:
                        return False
                    heapq.heappop(minheap)
        return True







            

        
        