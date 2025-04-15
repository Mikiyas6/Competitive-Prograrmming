class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openings = {"(","[","{"}
        parentheses = {")":"(","}":"{","]":"["}
        for value in s:
            if value not in openings:
                if stack and stack[-1] == parentheses[value]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(value)
        return True if not stack else False


            