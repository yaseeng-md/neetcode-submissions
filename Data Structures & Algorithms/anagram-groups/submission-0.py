from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counters = [Counter(s) for s in strs]

        visited = [False] * len(strs)
        ans = []

        for i in range(len(strs)):
            if visited[i]:
                continue

            group = [strs[i]]
            visited[i] = True

            for j in range(i + 1, len(strs)):
                if not visited[j] and counters[i] == counters[j]:
                    group.append(strs[j])
                    visited[j] = True

            ans.append(group)

        return ans