class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dictionary = {}
        lists = []
        for elements in cpdomains:
            lists = elements.split()
            amount = list(lists[1].split("."))
            for i in range(len(amount)):
                value = lists[1].split(".", i)
                usable = int(lists[0])
                if value[-1] in dictionary.keys():
                    dictionary[value[-1]] += usable
                else:
                    dictionary[value[-1]] = usable
            final_list = []
            for keys,values in dictionary.items():
                final_list.append(str(values)+" "+keys)
        return sorted(final_list)

        
