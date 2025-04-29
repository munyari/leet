"""
[1,2,5] [3,4]

[3,4] [1,2,5]
[3,4,1,2,5] i = 0 j = 2
[1,4,3,2,5]
"""
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1_back = m-1
        n2_back = n-1
        for l_back in range(n+m-1, -1, -1):
            if n2_back < 0:
                break
            if n1_back >= 0 and nums1[n1_back] > nums2[n2_back]:
                nums1[l_back] = nums1[n1_back]
                n1_back -= 1
            else:
                nums1[l_back] = nums2[n2_back]
                n2_back -= 1

def test_merge():
    s = Solution()
    l1 = [1,2,3,0,0,0]
    s.merge(l1, 3, [2,5,6], 3)
    assert l1 == [1,2,2,3,5,6], l1

test_merge()
