class Solution:
    def search(self, nums: List[int], target: int) -> int:

        s, e = 0, len(nums) - 1

        while s <= e:

            mid = (s+(e-s)//2)

            if nums[mid] == target:

                return mid

        #1 Checking whether the mid element is on the left or the right side
        #2 After knowing which side is the mid value part of, we then try to find which part we should look at

            if nums[mid] >= nums[s]: #Then the mid is part of the left side

                if target > nums[mid] or target < nums[s]:

                    s = mid + 1
                
                else:

                    e = mid - 1
            
            else: #Mid is part of the right side

                if target < nums[mid] or target > nums[e]:

                    e = mid - 1
                
                else:

                    s = mid + 1
        
        return -1

            