class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = l + (r - l) // 2
            t = 0
            for i in piles:
                t += math.ceil(i/m)
            if t <= h:
                res = min(res,m)
                r = m - 1
            else:
                l = m + 1
        return res