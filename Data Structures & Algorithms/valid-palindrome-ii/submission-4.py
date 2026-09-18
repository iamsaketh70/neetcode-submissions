class Solution:
    def palindrome(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True

    def validPalindrome(self, s: str) -> bool:

        l,r=0,len(s)-1
        count=0

        while l<r:
            while l<r and not(self.alphanumeric(s[l])):
                l+=1
            while l<r and not(self.alphanumeric(s[r])):
                r-=1
            if s[l]!=s[r]:
                return self.palindrome(s,l+1,r) or self.palindrome(s,l,r-1)
            
            l+=1
            r-=1

        return True
                
    def alphanumeric(self,c):
        return((ord('A')<=ord(c)<=ord('Z'))
         or (ord('a')<=ord(c)<=ord('z'))
          or (ord('0')<=ord(c)<=ord('9')))

        