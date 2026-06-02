class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        right = 0
        left = 0
        have = 0
        res = [-1,-1]
        res_length = float("inf")
        
        window = {}
        from collections import Counter
        t_count = Counter(t)
        need = len(t_count)
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0)+1

            if c in t_count and window[c] == t_count[c]:
                have +=1
            
            while have == need :
                if (right - left + 1) < res_length:
                    res = [left,right]
                    res_length = right - left +1
                
                window[s[left]] -= 1

                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -=1
                
                left += 1

        
        l,r = res
        return s[l:r+1] if res_length != float("inf") else ""


        

        
        

        