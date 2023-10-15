class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        from collections import Counter

        dictionary = Counter(p)
        
        i, j = 0, len(p)
        lists = []

        while j < len(s)+1:

            string = s[i:j] 
            new_dictionary = Counter(string)

            if new_dictionary == dictionary:
                lists.append(i)

            i += 1
            j += 1

        return lists
            

        
