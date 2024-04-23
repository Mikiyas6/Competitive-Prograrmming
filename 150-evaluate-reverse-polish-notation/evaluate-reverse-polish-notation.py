class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = "+-*/"

        stack = []

        for value in tokens:

            if value in operators:

                opperand1 = int(stack.pop())
                opperand2 = int(stack.pop())

                if value == "+":
                    
                    result = opperand2 + opperand1

                elif value == "-":
                    
                    result = opperand2 - opperand1

                elif value == "*":

                    result = opperand2 * opperand1

                else:

                    result = opperand2 / opperand1

                stack.append(result)
            
            else:

                stack.append(value)
        
        return int(stack[0])


