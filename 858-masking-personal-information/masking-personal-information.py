class Solution:
    def maskPII(self, s: str) -> str:

        if '@' in s:  # Email address
            name, domain = s.lower().split('@')
            return name[0] + '*****' + name[-1] + '@' + domain
        else:  # Phone number
            digits = re.findall(r'\d', s)
            local_number = '***-***-' + ''.join(digits[-4:])
            if len(digits) == 10:  # No country code
                return local_number
            else:  # With country code
                country_code = '+' + '*' * (len(digits) - 10) + '-'
                return country_code + local_number