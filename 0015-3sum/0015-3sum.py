class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        visited = set()
        result = []

        def findTarget(target,array):
            hashmap = defaultdict(int)
            visited = set()
            combos = []
            for value in array:
                if target - value in hashmap:
                    if (value,target-value) in visited:
                        continue
                    visited.add((value,target-value))
                    combos.append([-target,value,target-value])
                hashmap[value] += 1
            return combos

        for index in range(n-2):
            currValue = nums[index]
            if currValue in visited:
                continue
            visited.add(currValue)
            combos = findTarget(-currValue,nums[index+1:])
            for combo in combos:
                result.append(combo)

        return result

