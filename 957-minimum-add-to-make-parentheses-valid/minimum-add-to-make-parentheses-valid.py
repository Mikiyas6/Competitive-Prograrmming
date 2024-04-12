class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []
        counter = 0

        for char in s:

            if char == "(":

                stack.append(char)
                counter += 1
            
            else:

                if stack:

                    stack.pop()
                    counter -= 1
                
                else:

                    counter += 1
        
        return counter
        
