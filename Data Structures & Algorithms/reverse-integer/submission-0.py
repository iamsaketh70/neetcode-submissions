class Solution:
    def reverse(self, x: int) -> int:

        def rec(n:int,rev:int):
            if n==0:
                return rev
            rev=rev*10+n%10
            return rec(n//10,rev)

        sign=-1 if x <0 else 1
        n=abs(x)
        res=rec(n,0)
        res*=sign
        if res<-(1<<31) or res >(1<<31)-1:
            return 0
        return res



        

