class Solution:
    def partition(self, s: str) -> List[List[str]]:

        partitions = []

        def isPalindrome(string):
            return string == string[::-1]
        
        def dfs(i,part):

            if i == len(s):
                partitions.append(part[:])
                return 
            
            for j in range(i,len(s)):

                val = s[i:j+1]
                if isPalindrome(val):
                    part.append(val)
                    dfs(j+1,part)
                    part.pop()
        
        dfs(0,[])

        return partitions
            
        

