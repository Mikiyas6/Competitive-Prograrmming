class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashmap = defaultdict(int)
        for email in emails:
            local, domain = email.split("@")
            print("local->",local)
            print("domain->",domain)
            local = "".join(local.split("."))
            local = local.split("+")[0]
            print("local->",local)
            final_email = "@".join([local,domain])
            print("final_email->",final_email)
            hashmap[final_email] += 1
        return len(hashmap)