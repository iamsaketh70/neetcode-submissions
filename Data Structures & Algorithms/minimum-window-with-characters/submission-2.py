class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r=0,0
        res=[-1,-1]
        minlength=float("inf")
        t_count=Counter(t)
        need =len(t_count)
        count={}
        have=0

        for r in range(len(s)):
            index=s[r]
            count[s[r]]=count.get(s[r],0)+1

            if s[r] in t_count and count[s[r]]==t_count[s[r]]:
                have+=1
            
            while have==need:
                if r-l+1 < minlength:
                    res=[l,r]

                    minlength=r-l+1

                count[s[l]]-=1
                if s[l] in t_count and count[s[l]]<t_count[s[l]]:
                    have-=1
                l+=1
        left,right=res
        return s[left:right+1] if minlength!=float("inf") else ""
