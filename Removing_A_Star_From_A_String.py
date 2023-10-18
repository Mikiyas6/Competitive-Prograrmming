class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = []

        for letter in s:
            if letter != '*':
                stack.append(letter)
            else:
                stack.pop()
        
        return "".join(stack)
