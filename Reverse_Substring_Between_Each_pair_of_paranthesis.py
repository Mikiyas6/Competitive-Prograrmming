class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = str(s)
        stack = []
        list_of_string = list(string)
        i = 0
        while(i < len(list_of_string)):
            if (list_of_string[i] == "("):
                stack.append(i)
            elif (list_of_string[i] == ")"):
                add = stack[-1] + 1
                lis = list_of_string[add:i]
                for j in range(len(lis)//2):
                    lis[j], lis[len(lis) -1-j] = lis[len(lis) -1-j],lis[j]
                list_of_string[stack.pop():i+1] = lis
                i -= 2
            i += 1
        reversed = "".join(list_of_string)
        return reversed



                    
            
