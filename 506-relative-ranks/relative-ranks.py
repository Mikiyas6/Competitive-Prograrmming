class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        sorted_score = sorted(score)

        hashmap = defaultdict(int)

        for index, value in enumerate(sorted_score[::-1]):

            if index == 0:

                place = "Gold Medal"
            
            elif index == 1:

                place = "Silver Medal"
            
            elif index == 2:

                place = "Bronze Medal"
            
            else:

                place = str(index+1)

            hashmap[value] = place

        output = []

        for value in score:

            output.append(hashmap[value])
        
        return output

