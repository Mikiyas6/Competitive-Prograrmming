class Solution:
    def isValid(self, s: str) -> bool:
        
        opening = "([{"
        hashmap = {"(":")", "[":"]", "{":"}"}
        stack = []

        for char in s:

            if char in opening:

                stack.append(char)
            
            else:

                if stack and hashmap[stack[-1]] == char:

                    stack.pop()
                
                else:

                    return False
        
        return True if not stack else False