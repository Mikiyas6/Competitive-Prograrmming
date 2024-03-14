class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        string = "abcdefghijklmnopqrstuvwxyz"

        hashmap = defaultdict(str)

        for index in range(1,len(string)+1):

            if index < 10:

                hashmap[str(index)] = string[index-1]

            else:

                hashmap[str(index) + "#"] = string[index-1]
        
        new_string = ""

        i = len(s) - 1
        
        while i >= 0:

            print(s[i])

            if s[i-2] != '#':
                
                if s[i] == "#":

                    new_string += hashmap[s[i-2:i+1]]

                    i -= 3
                
                else:
                    
                    new_string += hashmap[s[i]]

                    i -= 1

            else:

                new_string += hashmap[s[i]] + hashmap[s[i-1]]

                i -= 2
        
        return new_string[::-1]




        
