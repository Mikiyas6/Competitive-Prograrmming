class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lists = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    index = j
                    if index == len(nums2)-1:
                            lists.append(-1)
                    else:
                        lists2 = nums2[index:]
                        print(lists2)
                        for k in range(len(lists2)):
                            if k == len(lists2)-1:
                                lists.append(-1)
                                break
                            elif (lists2[k+1] > lists2[0]):
                                lists.append(lists2[k+1])
                                break
                            elif (k+1 == len(lists2)-1) and (lists2[k+1] < lists2[0]):
                                lists.append(-1)
                                break
                            elif(lists2[k+1] < lists2[k+1] and k+1 != len(lists2)-1):
                                continue
                            else:
                                continue
        return lists
        
                    
