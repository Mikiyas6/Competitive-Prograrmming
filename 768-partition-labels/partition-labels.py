class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        hashmap = defaultdict(int)
        for index, value in enumerate(s):
            hashmap[value] = index
        
        checkPoint = hashmap[s[0]]
        n = len(s)
        result = [0]

        for index in range(n):

            if hashmap[s[index]] > checkPoint:
                checkPoint = hashmap[s[index]]

            if index == checkPoint:
                value =  index - sum(result) + 1
                result.append(value)
        
        return result[1:]