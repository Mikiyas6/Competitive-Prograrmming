class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = "+-*/"

        for token in tokens:

            if token in operators:

                operand1 = int(stack.pop())
                operand2 = int(stack.pop())

                if token == "+":

                    result = operand2 + operand1

                elif token == "-":

                    result = operand2 - operand1
                
                elif token == "*":

                    result = operand2 * operand1
                
                else:

                   result = operand2 / operand1

                stack.append(result)
            
            else:

                stack.append(token)
        
        return int(stack[0])

