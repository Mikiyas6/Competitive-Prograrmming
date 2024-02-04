class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        n = len(s)

        l = len(s) - 2
        r = len(s) - 1

        while l >= 0:

            if s[l] == " " and s[r] != " ":

                break
            
            l -= 1
            r -= 1

        counter = 0
        
        for i in range(r,n):

            if s[i] == " ":

                return counter
            
            counter += 1
        
        return counter
        
            
