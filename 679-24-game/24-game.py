class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def compute(a,b,op):
            if op==0:
                return a+b
            if op==1:
                return a-b
            if op==2:
                return a*b
            return a/b

        def solve(nums: List[int]):
            nonlocal solCount
            n = len(nums)
            if n==1:
                if goal-e < nums[0] < goal+e:
                    # print(sol)
                    solCount += 1
                return
            # stop at one solution
            if solCount>0:
                return
            for i in range(n):
                for j in range(n):
                    if i==j: continue
                    for op in range(3 + (nums[j]!=0)):
                        if i>j and op%2==0: continue
                        x = compute(nums[i], nums[j], op)
                        nums2 = [x]
                        for k in range(n):
                            if k!=i and k!=j:
                                nums2.append(nums[k])
                        # sol.append("%s = %s%s%s"%(x,nums[i],operator[op],nums[j]))
                        solve(nums2)
                        # sol.pop()

        e = 10**-5
        goal = 24
        operator = "+-*/"
        sol = []
        solCount = 0
        solve(cards)
        # print(solCount)
        return solCount>0