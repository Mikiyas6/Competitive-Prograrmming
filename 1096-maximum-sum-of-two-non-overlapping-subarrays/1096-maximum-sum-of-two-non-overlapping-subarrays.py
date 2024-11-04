class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], fl: int, sl: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        dps = [[0, 0] for _ in range(n + 1)]
        dpp = [[0, 0] for _ in range(n + 1)]

        s1 = sum(nums[:fl])
        dpp[fl][0] = s1
        rs1 = sum(nums[n-fl:n])
        dps[n-fl][0] = rs1
        for i in range(1, n - fl + 1):
            s1 = s1 + nums[i + fl - 1] - nums[i - 1]
            dpp[i + fl][0] = max(dpp[i + fl - 1][0], s1)
        
        for i in reversed(range(fl-1, n-1)):
            rs1 = rs1 + nums[i - fl + 1] - nums[i + 1]
            dps[i - fl + 1][0] = max(dps[i - fl + 2][0], rs1)

        s2 = sum(nums[:sl])
        dpp[sl][1] = s2
        rs2 = sum(nums[n-sl:n])
        dps[n-sl][1] = rs2
        for i in range(1, n - sl + 1):
            s2 = s2 + nums[i + sl - 1] - nums[i - 1]
            dpp[i + sl][1] = max(dpp[i + sl - 1][1], s2)
        
        for i in reversed(range(sl-1, n-1)):
            rs2 = rs2 + nums[i - sl + 1] - nums[i + 1]
            dps[i - sl + 1][1] = max(dps[i - sl + 2][1], rs2)

        res = 0
        shift = min(sl, fl)
        for i in range(shift - 1, n - shift + 1):
            res = max(res, dpp[i][0] + dps[i][1], dpp[i][1] + dps[i][0])

        return res