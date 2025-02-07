class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_total = 0
        for value in nums:
            if value %2 == 0:
                even_total += value
        result = []
        for value,index in queries:
            old_value = nums[index]
            nums[index] += value
            if nums[index] %2 == 0:
                even_total += value
                if old_value %2 != 0:
                    even_total += old_value
            else:
                if old_value %2 == 0:
                    even_total -= old_value
            result.append(even_total)
        return result
