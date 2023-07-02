class Solution:
    def isPalindrome(self, s: str) -> bool:
        lists = []
        for character in s:
            if character.isdigit() or character.isalnum():
                lists.append(character.lower())
        i = 0
        j = len(lists) - 1
        while i < len(lists)//2:
            if lists[i] != lists[j]:
                return False
            i += 1
            j -= 1
        return True
