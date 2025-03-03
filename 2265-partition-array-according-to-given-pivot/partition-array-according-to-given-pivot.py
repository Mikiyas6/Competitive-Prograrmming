class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = [num for num in nums if num < pivot]
        greater = [num for num in nums if num > pivot]
        equal = [num for num in nums if num == pivot]
        return less + equal + greater