class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap = Counter(arr)
        counter = 0
        for value in arr:
            if hashmap[value] == 1:
                counter += 1
                if counter == k:
                    return value
        return ''