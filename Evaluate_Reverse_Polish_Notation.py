class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = "+-*/"

        for char in tokens:

            if char not in operators:
                stack.append(char)
            
            else:

                operand1 = int(stack.pop())
                operand2 = int(stack.pop())

                if char == "+":
                    result = operand2 + operand1
                if char == "-":
                    result = operand2 - operand1
                if char == "*":
                    result = operand2 * operand1
                if char == "/":
                    result = operand2 / operand
                
                stack.append(result)
        
        return int(stack[0])
                
