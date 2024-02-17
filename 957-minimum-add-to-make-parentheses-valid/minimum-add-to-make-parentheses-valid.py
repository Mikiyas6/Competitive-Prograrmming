class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        moves = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    moves += 1

        moves += len(stack)
        return moves