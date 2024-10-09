class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []
        length = 0

        for char in s:

            if char == "(":

                stack.append(char)
                length += 1
            
            else:

                if stack and stack[-1] == "(":

                    stack.pop()
                    length -= 1
                
                else:

                    stack.append(char)
                    length += 1
        
        return length
        
