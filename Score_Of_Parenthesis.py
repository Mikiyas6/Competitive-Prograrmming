class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []

        for brace in s:

            if brace == "(":

                stack.append(0)
            
            else:

                total = 0
                removed = stack.pop()

                while removed > 0:

                    total += removed
                    removed = stack.pop()
                
                if total == 0:

                    total = 1
                
                else:

                    total *= 2
                
                stack.append(total)
        
        return sum(stack)
                  
