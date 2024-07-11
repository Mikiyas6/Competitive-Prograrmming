class Solution:
    def reverseParentheses(self, s: str) -> str:
        string = str(s)
        string = list(string)
        stack = []
        string_list = []
        reversed_string_list = []
        i = 0
        while(i < len(string)):
            if (string[i] == "("):
                stack.append(i)
            elif (string[i] == ")"):
                index_of_the_last_left_paranthesis = stack.pop()
                string_list = string[index_of_the_last_left_paranthesis+1:i]
                for j in range(len(string_list)):
                    reversed_string_list.append(string_list.pop())
                string[index_of_the_last_left_paranthesis:i+1] = reversed_string_list
                reversed_string_list = []
                i -= 2
            i += 1
        reversed_string = "".join(string)
        return reversed_string