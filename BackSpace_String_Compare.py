class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stack = []

        for char in s:

            print(stack)

            if char == "#": 
                if stack:
                    stack.pop()
            else:

                stack.append(char)
        
        string = "".join(stack)


        stack = []


        for char in t:

            if char == "#":
                if stack:
                    stack.pop()
            
            else:

                stack.append(char)
                

        if string == "".join(stack):
            return True
        
        return False

