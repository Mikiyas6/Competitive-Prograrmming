class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        hashmap = Counter(blocks[:k])
        if hashmap["B"] == k:
            return 0
        min_operation = hashmap["W"]
        left = 0
        for right in range(k,len(blocks)):
            hashmap[blocks[left]] -= 1
            hashmap[blocks[right]] += 1
            if hashmap["B"] == k:
                return 0
            min_operation = min(min_operation,hashmap["W"])
            left += 1
        return min_operation

