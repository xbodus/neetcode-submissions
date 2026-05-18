class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[str, list[str]] = {}

        for s in strs:
            s_key: str = str(sorted(s))
            groups.setdefault(s_key, []).append(s)
        
        return list(groups.values())