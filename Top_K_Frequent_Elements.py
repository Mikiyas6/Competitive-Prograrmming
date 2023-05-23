class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        lists = []
        dicts = {}
        counter = []
        listo = []
        for i in range(len(nums)):
            if nums[i] in dicts.keys():
                dicts[nums[i]].append(nums[i])
            else:
                dicts[nums[i]] = [nums[i]]
        for keys,values in dicts.items():
            counter.append((len(values),keys))
        for z in range(k):
            listo.append(max(counter)[1])
            counter.remove(max(counter))
        return(listo)
    
        

        


    
