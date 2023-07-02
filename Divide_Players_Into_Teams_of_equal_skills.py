class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Section One
        skill = sorted(skill)
        number_of_teams = len(skill)/2
        sum_of_individual_pair = sum(skill) // number_of_teams
        # Section Two
        i = 0
        j = len(skill) - 1
        list_of_pairs = []
        while i < j:
            print(i,j)
            if skill[i] + skill[j] == sum_of_individual_pair:
                list_of_pairs.append([skill[i],skill[j]])
            else:
                return -1
            i += 1
            j -= 1
        # Section Three
        total = 0
        for pair in list_of_pairs:
            total += pair[0]*pair[1]
        return total
