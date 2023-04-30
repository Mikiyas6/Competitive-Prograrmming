class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        list_of_poped_values = []
        dictionary = {}
        array = []
        for i in range(len(nums2)):
            if (len(stack) == 0):
                stack.append(nums2[i])
            else:
                while(len(stack) > 0):
                    if( nums2[i] <= stack[-1]):
                        stack.append(nums2[i])
                        break
                    elif (nums2[i] > stack[-1]):
                        list_of_poped_values.append(stack.pop(-1))
                        dictionary[nums2[i]] = list_of_poped_values 
                if len(stack) == 0:
                    stack.append(nums2[i])
                list_of_poped_values = []
        counter = 0
        for i in range(len(nums1)):
            for key,values in dictionary.items():
                if nums1[i] in values:
                    array.append(key)
                    counter = 0
                    break
                else:
                    counter += 1
            if counter == len(dictionary):
                array.append(-1)
                counter = 0
        return array
                    
        

        
               

            
                    
