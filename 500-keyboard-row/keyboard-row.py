class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        first_row = "qwertyuiop"

        second_row = "asdfghjkl"

        third_row = "zxcvbnm"

        keyboard = [first_row, second_row, third_row]

        output = []

        for word in words:

            word_set = set(word.lower())

            for row in keyboard:

                if word_set.issubset(row):

                    output.append(word)
        
        return output

            
        
        