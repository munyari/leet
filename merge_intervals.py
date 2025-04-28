from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda item: item[0])
        i = 0
        output = []
        while i < (len(intervals)):
            start, end = intervals[i]
            while i < len(intervals) and intervals[i][0] <= end:
                end = max(intervals[i][1], end)
                i += 1
            output.append([start, end])

        return output

def test_merge():
    sol = Solution()
    for case, expected in [
    ([[1,2], [2,3]], [[1,3]]),
    ([[1,4], [6,8], [4,5]], [[1,5], [6, 8]]),
    ([[2, 3], [2,3], [18,24]], [[2,3], [18,24]])
    ]:
        actual = sol.merge(case)
        assert actual == expected, f"{case=} {actual=}"

test_merge()

