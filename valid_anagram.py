class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_of_s = list(s)
        list_of_t = list(t)
        if len(list_of_t) != len(list_of_s):
            return False
        for letter in list_of_t:
            if letter not in list_of_s:
                return False
            else:
                list_of_s.remove(letter)
        return True
