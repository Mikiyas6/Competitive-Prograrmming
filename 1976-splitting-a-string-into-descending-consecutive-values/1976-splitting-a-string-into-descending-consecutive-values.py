class Solution:
    def splitString(self, s: str) -> bool:

        def dfs(i,prev):
            if i == len(s):
                return True
            
            for j in range(i,len(s)):
                string = int(s[i:j+1])
                if prev[-1] - string == 1:
                    prev.append(string)
                    if dfs(j+1,prev):
                        return True
                    prev.pop()
            
            return False

        prev = []
        for i in range(len(s)-1):

            string = int(s[:i+1])
            prev.append(string)
            if dfs(i+1,prev):
                return True
            prev.pop()
        
        return False


        # def dfs(i,splits):

        #     if i == len(s):
        #         if len(splits) == 1:
        #             return False

        #         inValue = splits[0]
        #         for value in splits[1:]:
        #             if inValue - value != 1:
        #                 return False
        #             inValue = value
                
        #         return True
            
        #     for j in range(i,len(s)):  # j is the ending of a split

        #         string = int(s[i:j+1])
        #         splits.append(string)
        #         if dfs(j+1,splits):
        #             return True
        #         splits.pop()
            
        #     return False
    
        
        # return dfs(0,[])


            
