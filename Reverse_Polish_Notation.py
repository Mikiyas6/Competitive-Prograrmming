class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        notations = tokens
        stack = []
        for character in notations:
            if str(character) != "+" and str(character) != "-" and str(character) != "/" and str(character) != "*":
                stack.append(int(str(character)))
            else:
                lists = []
                for i in range(2):
                    lists.append(stack.pop())
                print(lists)
                if character == "/":
                    result = lists[1] / lists[0]
                    if result > 0:
                        result = lists[1] // lists[0]
                    elif result < 0:
                        result = -1 *(abs(lists[1]) // abs(lists[0]))
                    stack.append(result)
                    continue
                    #     character = "//"
                    # else:
                    #     result = 0
                    #     stack.append(result)
                    #     continue
                result = (eval(str((lists[1]))+character+str(lists[0])))
                stack.append(result)
        return stack[0]
