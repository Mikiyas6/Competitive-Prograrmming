class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        # Calculate the score of each word
        def calculate_word_score(word):
            return sum(score[ord(char) - ord('a')] for char in word)

        word_scores = [calculate_word_score(word) for word in words]
        
        # Convert letters list to a Counter for easy manipulation
        letters_count = Counter(letters)
        
        def can_form_word(word, letters_count):
            word_count = Counter(word)
            for char in word_count:
                if word_count[char] > letters_count[char]:
                    return False
            return True
        
        def backtrack(index, current_score, letters_count):
            if index == len(words):
                return current_score
            
            # Option 1: Skip the current word
            max_score = backtrack(index + 1, current_score, letters_count)
            
            # Option 2: Include the current word if possible
            if can_form_word(words[index], letters_count):
                word_count = Counter(words[index])
                # Use the letters to form the word
                for char in word_count:
                    letters_count[char] -= word_count[char]
                
                # Recur with the next word
                max_score = max(max_score, backtrack(index + 1, current_score + word_scores[index], letters_count))
                
                # Backtrack to restore the letters_count
                for char in word_count:
                    letters_count[char] += word_count[char]
            
            return max_score
        
        return backtrack(0, 0, letters_count)