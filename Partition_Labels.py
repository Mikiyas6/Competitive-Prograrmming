class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        dictionary = {}

        for index,char in enumerate(s):

            dictionary[char] = index
        
        size = 0
        end = 0
        output = []

        for index,char in enumerate(s):

            end = max(end,dictionary[char])

            size += 1
            
            if end == index:
                output.append(size)
                size = 0
        
        return output
        
