class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        
        left_product = []
        right_product = [1]*n

        cumulative = 1

        for value in nums:

            left_product.append(cumulative)

            cumulative *= value
        
        cumulative = 1
        
        for index in range(n-1,-1,-1):

            right_product[index] = cumulative

            cumulative *= nums[index]
        
        product_except_self = []

        for index in range(n):

            product = left_product[index] * right_product[index]

            product_except_self.append(product)
        
        return product_except_self

