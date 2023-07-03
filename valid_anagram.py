class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # list_of_s = list(s)
        # list_of_t = list(t)
        # if len(list_of_t) != len(list_of_s):
        #     return False
        # for letter in list_of_t:
        #     if letter not in list_of_s:
        #         return False
        #     else:
        #         list_of_s.remove(letter)
        # return True
        if len(s) != len(t):
            return False
        dictionary_for_s = {}
        for letter in s:
            if letter not in dictionary_for_s.keys():
                dictionary_for_s[letter] = s.count(letter)
        for letter in t:
            if letter not in dictionary_for_s.keys() or t.count(letter) != dictionary_for_s[letter]:
                return False
        return True
