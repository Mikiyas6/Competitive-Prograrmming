class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        
        def backtrack(s,path):

            if not s:
                n = len(path)
                i,j = 0,1
                if j == n:
                    return False
                while j < n:
                    if int(path[i]) - int(path[j]) != 1:
                        return False
                    i += 1
                    j += 1
                return True

            for i in range(1,len(s)+1):
                path.append(s[:i])
                if backtrack(s[i:],path):
                    return True
                path.pop()

            return False
        
        return backtrack(s,[])
