class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for char in s:
            number = 0

            if char != "]":
                stack.append(char)
            
            else:

                string = []
                while stack[-1] != "[":

                    string.append(stack.pop())
                stack.pop()
                number = []
                while stack and stack[-1].isdigit():
                    number.append(stack.pop())
                string = string[::-1]
                number = number[::-1]
                number = "".join(number)
                n = int(number)
                string = "".join(string)
                string *= n
                stack.append(string)
        
        return "".join(stack)
