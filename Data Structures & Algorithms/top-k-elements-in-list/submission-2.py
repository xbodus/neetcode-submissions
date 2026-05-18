import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen: dict[int, int] = {}
        for n in nums:
            seen[n] = seen.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in seen.items():
            buckets[freq].append(num)

        top_k = []
        for i in range(len(buckets) - 1, 0, -1):
            for b in buckets[i]:
                top_k.append(b)
                if len(top_k) == k:
                    return top_k