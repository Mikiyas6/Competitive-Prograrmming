class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        word_set = set(words)  # Convert words to a set for efficient lookup
        longest_word = ""

        for word in sorted(words):  # Sort the words lexicographically
            if all(word[:i] in word_set for i in range(1, len(word))):  # Check if all prefixes are present
                if len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word):
                    longest_word = word

        return longest_word