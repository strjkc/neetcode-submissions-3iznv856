class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        items = {}
        for string in strs:
            sorted_string =''.join(sorted(string))
            if sorted_string not in items:
                items[sorted_string] = []
            items[sorted_string].append(string)
        return list(items.values())