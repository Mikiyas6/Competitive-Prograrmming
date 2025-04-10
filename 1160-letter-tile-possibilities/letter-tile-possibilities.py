class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.result = 0
        hashmap = Counter(tiles)
        def helper(hashmap,permute):
            for value in hashmap:
                result = 0
                if hashmap[value] > 0:
                    self.result += 1
                    permute.append(hashmap[value])
                    hashmap[value] -= 1
                    result += helper(hashmap,permute)
                    hashmap[value] += 1
                self.result += result
            return result
        helper(hashmap,[])
        return self.result