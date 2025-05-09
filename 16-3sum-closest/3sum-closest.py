class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        n = len(nums)
        closest_sum = float("inf")
        minimum_distance = float("inf")

        for k in range(len(nums)):
            i = k + 1
            j = n - 1

            while i < j:
                current_sum = nums[k] + nums[i] + nums[j]
                new_distance = abs(target - current_sum)

                if new_distance < minimum_distance:
                    closest_sum = current_sum
                    minimum_distance = new_distance

                if current_sum == target:
                    return closest_sum
                elif current_sum < target:
                    i += 1
                else:
                    j -= 1

        return closest_sum

