class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checked = {}

        for s in strs:
            key = "".join(sorted(s))
            if key not in checked:
                checked[key] = []
            checked[key].append(s)
        
        return list(checked.values())