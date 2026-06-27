class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        s_c = Counter(s)
        t_c = Counter(t)
        if s_c == t_c:
            return True
        else:
            return False