class Solution:
    def isPalindrome(self, s: str) -> bool:
        reformed = ''.join(re.findall(r'[A-Za-z0-9]', s)).lower()
        left = 0
        right = len(reformed)-1
        while left <= right:
            if reformed[left] != reformed[right]:
                return False
            left += 1
            right -= 1
        return True
       