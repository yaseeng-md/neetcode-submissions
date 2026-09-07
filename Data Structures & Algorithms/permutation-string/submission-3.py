from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)

        if window_size > len(s2):
            return False

        target = Counter(s1)
        window = Counter(s2[:window_size])

        if window == target:
            return True

        left = 0

        for right in range(window_size, len(s2)):
            # Add new character
            window[s2[right]] += 1

            # Remove old character
            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            left += 1

            if window == target:
                return True

        return False