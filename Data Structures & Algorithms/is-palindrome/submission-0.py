
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        result = re.sub(r'[^a-zA-Z0-9]', '', s)
        result = result.lower()
        for i in range(len(result) // 2):
            strt_pointer = i
            end_pointer = len(result) - i - 1
            if not result[strt_pointer] == result[end_pointer]:
                return False
        return True