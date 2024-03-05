class Solution:
    def sortSentence(self, s: str) -> str:
        
        words = s.split()
        word_dict = {}

        for word in words:
            position = int(word[-1])
            word_dict[position] = word[:-1]

        sorted_words = [word_dict[i] for i in range(1, len(words)+1)]
        original_sentence = " ".join(sorted_words)

        return original_sentence