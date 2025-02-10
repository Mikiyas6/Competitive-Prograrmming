class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap = defaultdict(int)
        for cpdomain in cpdomains:
            visit_times,domain = cpdomain.split()
            visit_times = int(visit_times)
            splitted_domain = domain.split(".")
            n = len(splitted_domain)
            for i in range(n):
                hashmap[".".join(splitted_domain[i:])] += visit_times
        result = []
        for key,value in hashmap.items():
            result.append(f"{value} {key}")
        return result
