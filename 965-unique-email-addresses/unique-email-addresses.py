class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.split('+')[0].replace('.', '')
            unique_emails.add(local_name + '@' + domain_name)
        return len(unique_emails)