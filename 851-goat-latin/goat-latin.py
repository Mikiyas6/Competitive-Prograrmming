class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        
        def is_vowel(char):
            return char.lower() in ['a', 'e', 'i', 'o', 'u']

        def goatify(word, index):
            if is_vowel(word[0]):
                return word + 'ma' + 'a' * (index + 1)
            else:
                return word[1:] + word[0] + 'ma' + 'a' * (index + 1)

        words = sentence.split()
        result_words = [goatify(word, i) for i, word in enumerate(words)]
        return ' '.join(result_words)