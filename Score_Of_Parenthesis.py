class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []

        for char in s:

            if char == "(":

                stack.append(-1)
            
            else:

                i = -1
                total = 0

                while stack[i] != -1:

                    total += stack[i]

                    i -= 1
                
                if total != 0:
                    total = total * 2
                if total == 0:
                    total = 1

                stack[i] = total
                stack = stack[:len(stack)+i+1]
    

            
        return sum(stack)
            
