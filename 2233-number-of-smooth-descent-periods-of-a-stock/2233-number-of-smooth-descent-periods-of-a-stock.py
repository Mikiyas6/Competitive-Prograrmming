class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = cnt = 0
        prev = -math.inf
        for cur in prices:
            if prev - cur == 1:
                cnt += 1
            else:
                cnt = 1
            ans += cnt
            prev = cur
        return ans
        