class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hashmap = defaultdict(list)
        for digit in nums:
            total = 0
            temp = digit
            while temp != 0:
                total += temp%10
                temp //= 10
            hashmap[total].append(digit)
        max_sum = 0
        for values in hashmap.values():
            if len(values) >= 2:
                values.sort()
                result = values[-1] + values[-2]
                max_sum = max(max_sum,result)
        return max_sum if len(nums) != len(hashmap) else -1

            