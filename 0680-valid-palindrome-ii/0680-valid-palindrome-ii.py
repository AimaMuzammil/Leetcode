
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s)-1
        while (r>l):
            if s[l]!=s[r]:
               return (self.almostPalindromic (s , l+1 , r) or self.almostPalindromic(s, l , r-1)) 
            l+=1
            r-=1
        return True
    def almostPalindromic(self, s , l , r):
        while (l<r ):
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True       