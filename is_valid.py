class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {"(":")", "[":"]", "{":"}"} 
        symbool = str(s)
        lists = []
        for char in symbool: 
            if char == "(" or char == "[" or char == "{": 
                lists.append(char)
            else: 
                if len(lists) == 0:
                    return False
                elif dict[lists[-1]] == char:
                    lists.pop()
                else:
                    return False        
        print(lists)
        if len(lists) == 0:
            return True
        else:
            return False
