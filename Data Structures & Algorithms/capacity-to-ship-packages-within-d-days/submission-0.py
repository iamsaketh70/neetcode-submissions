class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=float("inf")

        def canship(mid):
            ship,cap=1,mid
            for weight in weights:
                if cap-weight<0:
                    ship+=1
                    cap=mid
                cap-=weight
            return ship<=days
                    
        while l<=r:
            mid=(l+r)//2
            if canship(mid):
                res=min(res,mid)
                r=mid-1

            else:
                l=mid+1
        return res


        