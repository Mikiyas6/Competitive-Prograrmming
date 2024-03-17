class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        lists = []
        start = 0
        end = len(nums) - 1
        if not nums:
            return [-1,-1]
        elif len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        while end >= start:
            if nums[start] == target and start not in lists:
                lists.append(start)
            if nums[end] == target and end not in lists:
                lists.append(end)
            middle = start + (end-start)//2
            if target > nums[middle]:
                start = middle +  1
            elif target < nums[middle]:
                end = middle - 1
            elif target == nums[middle] and middle not in lists:
                lists.append(middle)
                if nums[middle + 1] != target:
                    end = middle
                elif nums[middle - 1] != target:
                    start = middle
                else:
                    start += 1
                    end -= 1
            else:
               start += 1
               end -= 1
        lists = sorted(lists)
        if not lists:
            return [-1,-1]
        else:
            return [lists[0],lists[-1]]
        