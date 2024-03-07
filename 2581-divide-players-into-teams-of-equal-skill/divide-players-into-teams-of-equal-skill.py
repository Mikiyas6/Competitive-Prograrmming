class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort() #O(nlogn)

        n = len(skill)

        i = 0
        j = n - 1

        target = skill[i] + skill[j]

        total = skill[i] * skill[j]

        i += 1
        j -= 1

        while i < j: #O(n)

            if skill[i] + skill[j] == target:

                total += skill[i] * skill[j]

            else:

                return -1

            i += 1
            j -= 1

        return total

        # Time complexity = O(nlogn) + O(n) = O(nlogn)
        
        # Space Complexity = O(1)