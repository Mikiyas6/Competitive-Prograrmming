class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        lists = list(s)
        new_string = ""
        for i in range(len(spaces)):
            if new_string == "":
                new_string = s[:spaces[i]] + " "
            else:
                new_string += s[spaces[i-1]:spaces[i]] + " "
        new_string += s[spaces[i]:]
        return new_string
        