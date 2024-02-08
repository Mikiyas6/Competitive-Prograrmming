class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target_3 = target - nums[i]
            for j in range(i + 1, n - 2):
                # Skip duplicates
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left, right = j + 1, n - 1
                while left < right:
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if four_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        # Skip duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif four_sum < target:
                        left += 1
                    else:
                        right -= 1

        return result
