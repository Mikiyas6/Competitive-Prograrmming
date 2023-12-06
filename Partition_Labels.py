class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        hashmap = defaultdict(int)

        for index,letter in enumerate(s):

            hashmap[letter] = index
        
        counter = 0

        end = 0

        output = []
        
        for index,letter in enumerate(s):

            end = max(end,hashmap[letter])

            counter += 1

            if index == end:

                output.append(counter)

                counter = 0
        
        return output


        # hashmap = defaultdict(list)

        # for index,value in enumerate(s):

        #     hashmap[value].append(index)
    
        # for letter,indexes in hashmap.items():

        #     if len(indexes) < 2:

        #         start = indexes[0]
            
        #     else:

        #         start = indexes[0]
        #         end = indexes[-1]

        #         hashmap[letter] = [start,end]
        
        # starting = hashmap[s[0]][0]

        # if len(hashmap[s[0]]) > 1:
        
        #     ending = end =  hashmap[s[0]][1]
        
        # else:

        #     ending = starting

        # output = []

        # for indexes in hashmap.values():

        #     start = indexes[0]

        #     if start > ending:

        #         output.append(ending - starting + 1)
                
        #         starting = start

        #         if len(indexes) > 1:
        #             ending = indexes[1]
            
        #     if len(indexes) > 1:

        #         end = indexes[1]

        #         ending = max(ending,end)
            
        #     else:

        #         ending = max(ending,start)
        
        # output.append(ending - starting + 1)
        
        # return output

            


                
        

