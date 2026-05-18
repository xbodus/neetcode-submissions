import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen: dict[int, int] = {}
        for n in nums:
            seen[n] = seen.get(n, 0) + 1

        top_k = dict(list(heapq.nlargest(k, seen.items(), key=lambda i: i[1]))).keys()
        return list(top_k)