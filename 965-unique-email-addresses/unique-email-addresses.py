class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashmap = defaultdict(int)
        for email in emails:
            local, domain = email.split("@")
            local = "".join(local.split("."))
            local = local.split("+")[0]
            final_email = "@".join([local,domain])
            hashmap[final_email] += 1
        return len(hashmap)