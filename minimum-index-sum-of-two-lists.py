class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        hashmap1 = defaultdict(int)
        hashmap2 = defaultdict(int)

        for index, value in enumerate(list1):

            hashmap1[value] = index
        
        for index, value in enumerate(list2):

            hashmap2[value] = index
        
        set_1 = set(list1)
        set_2 = set(list2)

        set_3 = set_1 & set_2

        list3 = list(set_3)

        least_index = float("inf")

        hashmap3 = defaultdict(int)

        for value in list3:

            result = hashmap1[value] + hashmap2[value]

            least_index = min(least_index,result)

            hashmap3[value] = result

        output = []

        for value in hashmap3:

            if hashmap3[value] == least_index:

                output.append(value)
        
        return output


