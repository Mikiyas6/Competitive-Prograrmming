class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        removed = 0
        
        for digit in num:
            while stack and stack[-1] > digit and removed < k:
                stack.pop()
                removed += 1
            stack.append(digit)
        
        # If k is not exhausted, remove the remaining digits from the end
        while removed < k:
            stack.pop()
            removed += 1
        
        # Remove leading zeroes
        while stack and stack[0] == '0':
            stack.pop(0)
        
        return ''.join(stack) if stack else '0'