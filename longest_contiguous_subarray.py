from typing import List
import heapq

class Solution:
    def longestSubarray2(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        matrix = [[(False,-1,-1) for _ in range(0, n)] for _ in range(0, n)]
        for i in range(0, n):
            matrix[i][i] = (True, nums[i], nums[i])

        longest = 1
        for i in range(0, n):
            for j in range(i+1, n):
                prev = matrix[i][j-1]
                is_valid_subarray = prev[0] and abs(nums[j]-prev[1]) <= limit and abs(nums[j]-prev[2]) <= limit
                max_in_subarray = max(prev[1], nums[j])
                min_in_subarray = min(prev[2], nums[j])
                if is_valid_subarray:
                    longest = max(longest, j-i+1)
                matrix[i][j] = (is_valid_subarray, max_in_subarray, min_in_subarray)

        return longest

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        longest = 0
        left = 0
        min_heap = []
        max_heap = []
        for right in range(0, n):
            heapq.heappush(min_heap, (nums[right], right))
            heapq.heappush(max_heap, (-nums[right], right))
            while -max_heap[0][0] - min_heap[0][0] > limit:
                left = min(max_heap[0][1], min_heap[0][1]) + 1
                while max_heap[0][1] < left:
                    heapq.heappop(max_heap)

                while min_heap[0][1] < left:
                    heapq.heappop(min_heap)

            longest = max(longest, right-left+1)

        return longest

def test_longest_subarray():
    for case, limit, expected in [
        ([12], 1, 1),
        ([0,1,0,2,1,0,1,3,2,1,2,1], 1, 4),
    ]:
        s = Solution()
        actual = s.longestSubarray(case, limit)
        assert actual == expected, f"{case=} {actual=} {expected=}"
    print("Tests passed")

test_longest_subarray()
