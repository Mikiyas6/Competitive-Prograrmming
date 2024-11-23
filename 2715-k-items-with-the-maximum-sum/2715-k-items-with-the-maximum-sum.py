class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # array = []
        # for i in range(numOnes):
        #     array.append(1)
        # for i in range(numZeros):
        #     array.append(0)
        # for i in range(numNegOnes):
        #     array.append(-1)
        # return sum(array[:k])

        ans = min(numOnes,k)
        k -= numOnes
        if k <= 0:
            return ans
        k -= numZeros
        if k <= 0:
            return ans
        ans -= min(k,numNegOnes)
        return ans