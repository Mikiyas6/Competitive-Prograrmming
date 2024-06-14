class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        hashmap = defaultdict(int)

        for index, value in enumerate(order):
            hashmap[value] = index
        
        i, j = 0, 1
        while j < len(words):
            word1 = words[i]
            word2 = words[j]

            a, b = 0, 0
            a_size, b_size = len(word1), len(word2)

            while a < a_size and b < b_size:
                if hashmap[word1[a]] > hashmap[word2[b]]:
                    return False
                if hashmap[word1[a]] < hashmap[word2[b]]:
                    break
                a += 1
                b += 1
            
            if a < a_size and b >= b_size:
                return False
            
            i += 1
            j += 1
        
        return True
        
            
