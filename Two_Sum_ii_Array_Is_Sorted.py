class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        if len(numbers) < 2:
            return []

        i = 0
        j = len(numbers) - 1
        lists = []

        while i < j:

            if numbers[i] + numbers[j] == target:
                lists.extend([i+1,j+1])
                i += 1
                j -= 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        
        return lists
