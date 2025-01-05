class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dicts = {}
        dicto = {}
        listings = []
        count = 0
        current = None
        freq = []
        arr = self.Counting_sort(arr)
        for i in range(len(arr)):
            if arr[i] == current:
                count += 1
            else:
                if i > 0:
                    freq.append(count)
                current = arr[i]
                count = 1
        freq.append(count)
        print(freq)
        listings = self.Counting_sort(freq) 
        pins = []
        for i in range(len(listings)):
            pins.append(listings.pop())
        listings = pins
        print(listings)
        total = 0
        counter = 0
        for j in range(len(listings)):
            total += listings[j]
            counter += 1
            if total >= len(arr)/2.0:
                return counter
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