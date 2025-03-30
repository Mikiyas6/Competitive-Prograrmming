class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        hashmap = Counter(blocks[:k])
        min_operations = hashmap['W']
        left = 0
        for right in range(k,len(blocks)):
            hashmap[blocks[right]] += 1
            hashmap[blocks[left]] -= 1
            min_operations = min(min_operations,hashmap["W"])
            left += 1
        return min_operations 