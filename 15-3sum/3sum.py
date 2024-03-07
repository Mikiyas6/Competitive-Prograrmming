class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        n = len(nums)

        hashset = set()

        for k in range(n):

            i = k + 1
            j = n - 1

            complement = -1 * nums[k]

            while i < j:

                summation = nums[i] + nums[j]

                if summation == complement:

                    hashset.add((nums[k],nums[i],nums[j]))
                    i += 1
                    j -= 1
                
                elif summation < complement:

                    i += 1
                
                else:

                    j -= 1
            
        output = list(map(list,hashset))

        return output

