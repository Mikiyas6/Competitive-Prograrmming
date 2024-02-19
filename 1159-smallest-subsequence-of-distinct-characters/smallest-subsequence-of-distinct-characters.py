class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        stack = []
        last_occurrence = {char: i for i, char in enumerate(s)}
        used_chars = set()
        
        for i, char in enumerate(s):
            if char in used_chars:
                continue
            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                used_chars.remove(stack.pop())
            stack.append(char)
            used_chars.add(char)
        
        return ''.join(stack)