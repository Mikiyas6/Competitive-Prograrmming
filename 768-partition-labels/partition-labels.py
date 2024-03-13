class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        hashmap = defaultdict(int)

        for index, value in enumerate(s):

            hashmap[value] = index
        
        partition_end = 0

        counter = 0

        lists = []
        
        for index, value in enumerate(s):

            partition_end = max(partition_end,hashmap[value])

            counter += 1

            if partition_end == index:

                lists.append(counter)

                counter = 0
        
        return lists