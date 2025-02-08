class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = 0
        hashmap = Counter(chars)
        for word in words:
            hashmap_inner = Counter(word)
            flag = False
            for value in hashmap_inner:
                if not hashmap[value] or hashmap_inner[value] > hashmap[value]:
                    flag = True
                    break
            if not flag:
                counter += len(word)
        return counter