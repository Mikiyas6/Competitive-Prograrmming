class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams_dict = {}

        for word in strs:
            # Sort the characters in the word to identify anagrams
            sorted_word = ''.join(sorted(word))

            # Check if the sorted word is already a key in the dictionary
            if sorted_word in anagrams_dict:
                anagrams_dict[sorted_word].append(word)
            else:
                # If not, create a new key with the sorted word and a list containing the word
                anagrams_dict[sorted_word] = [word]

        # Convert values of the dictionary to a list to get the final result
        result = list(anagrams_dict.values())
        
        return result
