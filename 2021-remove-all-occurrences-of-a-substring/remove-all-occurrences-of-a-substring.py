class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n = len(part)
        for value in s:
            stack.append(value)
            while stack and "".join(stack[-n:]) == part:
                for _ in range(n):
                    stack.pop()
        return "".join(stack)
            