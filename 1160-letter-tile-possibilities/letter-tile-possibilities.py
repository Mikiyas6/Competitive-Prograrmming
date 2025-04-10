class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.result = 0
        hashmap = Counter(tiles)
        def helper(hashmap):
            for value in hashmap:
                result = 0
                if hashmap[value] > 0:
                    self.result += 1
                    hashmap[value] -= 1
                    result = helper(hashmap)
                    hashmap[value] += 1
                    self.result += result
            return result
        helper(hashmap)
        return self.result