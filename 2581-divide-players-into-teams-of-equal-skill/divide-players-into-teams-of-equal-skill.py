class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        n = len(skill)
        skill.sort()

        left = 0
        right = n-1
        total = 0

        value = skill[left] + skill[right]

        while left < right:
            if skill[left] + skill[right] != value:
                return -1
            total += skill[left] * skill[right]
            left += 1
            right -= 1

        return total