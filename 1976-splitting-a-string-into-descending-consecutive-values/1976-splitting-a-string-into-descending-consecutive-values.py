class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        
        def backtrack(s,path):
            if not s:
                if len(path) == 1:
                    return False
                return True
                
            for i in range(1,len(s)+1):
                if not path or int(path[-1]) - int(s[:i]) == 1:
                    path.append(s[:i])
                    if backtrack(s[i:],path):
                        return True
                    path.pop()

            return False
        
        return backtrack(s,[])
