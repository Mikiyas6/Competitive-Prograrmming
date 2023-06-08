class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles = self.Counting_sort(piles)
        pint = []
        for i in range(len(piles)):
            pint.append(piles.pop())
        piles = pint
        total = 0
        for i in range(len(piles)/3):
            total += piles[2*i + 1]
        return total
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


        
