class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        hashmap = defaultdict(int)

        for index, value in enumerate(s):

            hashmap[value] = index
        
        output = []

        farthest = 0

        counter = 0
        
        for index, value in enumerate(s):

            farthest = max(farthest,hashmap[value])

            counter += 1

            if farthest == index:

                output.append(counter)

                counter = 0
        
        return output
