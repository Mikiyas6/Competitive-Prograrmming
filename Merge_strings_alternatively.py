class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        string = ""

        min_length = min(len(word1),len(word2))

        for i in range(min_length):

            string += word1[i] + word2[i]
        
        return string + word1[i+1:] + word2[i+1:]
