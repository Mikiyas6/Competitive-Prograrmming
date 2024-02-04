class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        keyboard_rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result = []

        for word in words:
            word_lower = word.lower()

            if any(all(char in row for char in word_lower) for row in keyboard_rows):
                result.append(word)

        return result
