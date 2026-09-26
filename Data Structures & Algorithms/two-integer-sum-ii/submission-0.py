class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(numbers, 1):
            diff = target - n
            if diff in dic:
                return [dic[diff], i]
            dic[n] = i
        