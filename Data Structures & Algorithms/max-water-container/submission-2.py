class Solution:
    def maxArea(self, heights: List[int]) -> int:
        vol = 0
        l, r = 0, len(heights) - 1
        while l < r:
            vol = max(vol, min(heights[l], heights[r]) * (r - l))
            if heights[r] > heights[l]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                r -= 1
                l += 1
        return vol