class Solution:
    def reverseWords(self, s: str) -> str:
        
        s.strip()

        list_of_words = s.split()

        list_of_words = list_of_words[::-1]

        return " ".join(list_of_words)