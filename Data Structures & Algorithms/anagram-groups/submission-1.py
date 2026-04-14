class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            sorted_w = ''.join(sorted(word))
            if sorted_w in groups:
                groups[sorted_w].append(word)
            else:
                groups[sorted_w] = [word]
        return list(groups.values())