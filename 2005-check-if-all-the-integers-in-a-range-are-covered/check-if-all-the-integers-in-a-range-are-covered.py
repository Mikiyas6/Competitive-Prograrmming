class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        max_value = 0
        for x, y in ranges:
            max_value = max(max_value,y)
        prefixSum = [0]*(max_value+1)
        for x, y in ranges:
            prefixSum[x-1] += 1
            prefixSum[y] -= 1
        total = 0
        for i in range(len(prefixSum)-1):
            total += prefixSum[i]
            prefixSum[i] = total
        if left > max_value or right > max_value:
            return False
        print(prefixSum)
        for i in range(left-1,right):
            if prefixSum[i] < 1:
                return False
        return True