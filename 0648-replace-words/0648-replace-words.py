class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Convert dictionary to a set for fast lookup
        root_set = set(dictionary)
        
        def replace_word(word):
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in root_set:
                    return prefix
            return word
        
        # Split the sentence into words
        words = sentence.split()
        
        # Replace each word with its root if possible
        replaced_words = [replace_word(word) for word in words]
        
        # Join the replaced words to form the final sentence
        return ' '.join(replaced_words)