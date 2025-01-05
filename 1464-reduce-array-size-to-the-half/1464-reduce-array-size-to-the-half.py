class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        hashmap = Counter(arr)
        match = [(value,key) for key,value in hashmap.items()]
        match.sort()
        n = len(arr)
        total = 0
        limit = n//2
        for i in range(len(match)-1,-1,-1):
            freq,value = match[i]
            total += freq
            if total >= limit:
                print(i,total)
                break
        return len(match)-i
        