Given a string s, return the longest palindromic substring  in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        resLength = 0
        for i in range(len(s)):
            l = r = i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > resLength:
                    res = s[l:r+1]
                    resLength = r-l+1
                l -=1
                r +=1
            l = i 
            r = i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > resLength:
                    res = s[l:r+1]
                    resLength = r-l+1
                l -=1
                r +=1
        return res
                
