class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen: dict[int, int] = {}
        for n in nums:
            seen[n] = seen.get(n, 0) + 1
        
        return list(dict(sorted(seen.items(), key=lambda item : -item[1])).keys())[:k]