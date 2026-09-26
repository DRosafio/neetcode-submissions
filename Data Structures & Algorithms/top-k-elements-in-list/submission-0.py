class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res =[]
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for i in range(k):
            res.append(max(count, key=count.get))
            count.pop(max(count, key=count.get))
        return res