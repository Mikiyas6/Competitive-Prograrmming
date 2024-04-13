class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        for char in num:

            while k > 0 and stack and char < stack[-1]:

                k -= 1
                stack.pop()
            
            stack.append(char)
        
        if k > 0:

            stack = stack[:len(stack)-k]

        while stack and stack[0] == "0":

            stack.pop(0)
        
        return "".join(stack) if stack else "0"


        