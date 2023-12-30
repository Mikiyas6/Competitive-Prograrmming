class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = []
        
        for value in s:

            if value == "(":

                stack.append(0)
            
            else:

                total = 0

                while stack and stack[-1] != 0:

                    total += 2 * stack.pop()

                stack[-1] = total if total != 0 else 1
        
        return sum(stack)
