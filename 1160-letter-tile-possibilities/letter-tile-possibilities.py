class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.result = 0
        hashmap = Counter(tiles)
        def helper(hashmap):
            result = 0
            for value in hashmap:
                if hashmap[value] > 0:
                    self.result += 1
                    hashmap[value] -= 1
                    result = helper(hashmap)
                    self.result += result
                    hashmap[value] += 1
            return result
        helper(hashmap)
        return self.result