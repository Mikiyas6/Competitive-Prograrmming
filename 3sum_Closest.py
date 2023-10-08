class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()

        lists = []

        for k in range(len(nums)):

            key = nums[k]
            i = k + 1
            j = len(nums) - 1

            while i < j:

                if key + nums[i] + nums[j] == target:
                    lists.append(key + nums[i] + nums[j])
                    i += 1
                    j -= 1
                elif key + nums[i] + nums[j] > target:
                    lists.append(key + nums[i] + nums[j])
                    j -= 1
                else:
                    lists.append(key + nums[i] + nums[j])
                    i += 1
        
        dictionary = {}
            
        new_list = []

        for value in lists:

            distance = target - value

            if distance < 0:
                distance = -1 * distance
            
            new_list.append(distance)
            dictionary[distance] = value
        
        return dictionary[min(new_list)]
    
