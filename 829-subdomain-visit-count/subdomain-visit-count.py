class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        hashmap = defaultdict(int)

        for cpdomain in cpdomains:

            number_of_visit, domains = cpdomain.split()

            number_of_visit = int(number_of_visit)

            domains = domains.split(".")

            for i in range(len(domains)-1,-1,-1):

                domain = ".".join(domains[i:])

                hashmap[domain] += number_of_visit
        
        output = []

        for value in hashmap:

            answer = " ".join([str(hashmap[value]), value])

            output.append(answer)
        
        return output