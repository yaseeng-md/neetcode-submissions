from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        print(window_size)
        counter = Counter(s1)
        print(counter)
        i = 0

        while i + window_size <= len(s2):
            temp_counter = Counter(s2[i:i+window_size])
            print(temp_counter)
            if temp_counter == counter:
                return True
            i += 1
        return False
