class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[-1] == target:
                return True
            if i[-1] > target:
                j, k = 0, len(i) - 1
                while j <= k:
                    m = (j + k) // 2
                    if i[m] > target:
                        k = m - 1
                    elif i[m] < target:
                        j = m + 1
                    else:
                        return True
        return False