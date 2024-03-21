class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:

        n = len(word)

        if n < 5:

            return 0

        longest = 0

        hashset = set()

        hashmap = {"a":["a"],"e":["e","a"],"i":["e","i"],"o":["i","o"],"u":["o","u"]}

        counter = 1

        r = 1

        while r < n:

            while r < n and word[r-1] in hashmap[word[r]]:

                counter += 1

                hashset.add(word[r-1])
                hashset.add(word[r])

                r += 1
            
            if word[r-1] != "u" or len(hashset) < 5:

                counter = 1
            
            longest = max(longest,counter)

            counter = 1

            r += 1

            hashset = set()
        
        return longest if longest >= 5 else 0













            




        
