class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        changed = self.Counting_sort(changed)
        lists = []
        a = 0
        b = 1
        matched = []
        unmatched = []
        pointer = 0
        print(changed)
        for i in range(len(changed)):
            if len(unmatched) > pointer:
                if 2*unmatched[pointer] == changed[i]:
                    matched.append(unmatched[pointer])
                    pointer += 1
                else:   
                    unmatched.append(changed[i])
            else:
                unmatched.append(changed[i])
        if pointer < len(unmatched):
            return []
        else:
            return matched
    def Counting_sort(self,nums):
        lists1 = [0] * (max(nums)+1)
        for i in range(len(nums)):
            lists1[nums[i]] += 1
        lists2 = []
        for i in range(len(lists1)):
            if i == 0:
                lists2.append(lists1[i])
            else:
                lists2.append(lists1[i]+lists2[-1])
        lists3 = [0] * (len(nums))
        for i in range(len(nums)):
            lists3[lists2[nums[i]]-1] = nums[i]
            lists2[nums[i]] = lists2[nums[i]] - 1
        return lists3