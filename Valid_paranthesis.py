class Solution:
    def isValid(self, s: str) -> bool:
        
        braces = { ")":"(", "}":"{", "]":"["}
        opening_brace = "({["

        stack = []

        if len(s) == 1:

            return False

        for brace in s:

            if brace in opening_brace:

                stack.append(brace)
            
            else:

                if stack and braces[brace] == stack[-1]:

                    stack.pop()
                
                else:

                    return False
            
        return True if not stack else False


        
