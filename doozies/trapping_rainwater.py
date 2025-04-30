from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        vol = 0
        i = 0
        while i < len(height): # i = 7 height = [0,1,0,2,1,0,1,3,2,1,2,1]
            r = i + 1 # r = 8
            max_r = r # max_r = 8
            while r < len(height): # r = 11
                if height[max_r] <= height[r]: # false
                    max_r = r # 9
                if height[r] >= height[i]: # false
                    break
                r += 1 # r = 11

            r_height = min(height[i], height[max_r]) # 2
            for v in range(i+1, r): # v = 7
                add_vol = r_height-height[v] # 2-1 = 1
                if add_vol > 0:
                    print(f"{i=} {r=} {add_vol=}")
                    vol += add_vol # 5

            print(f"{i=} {r=} {vol=}")
            i = r # i = 7


        return vol

    def trap2(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        vol = 0
        maxs_l = [0] * len(height)
        maxs_l[0] = height[0]
        for i in range(1, len(height)):
            maxs_l[i] = max(height[i], maxs_l[i-1])
        
        maxs_r = [0] * len(height)
        maxs_r[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            maxs_r[i] = max(height[i], maxs_r[i+1])

        for i in range(0, len(height)-1):
            vol += min(maxs_l[i], maxs_r[i]) - height[i]

        return vol

    def trap3(self, height: List[int]) -> int:
        vol = 0
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        while left < right: # left = 3, right = 10
            if height[left] < height[right]: # true
                left_max = max(left_max, height[left]) # 1
                vol += left_max - height[left] # 1
                left += 1 # 3
            else:
                right_max = max(right_max, height[right]) # 2
                vol += right_max - height[right] # 0
                right -= 1 # 10
        return vol

    def trap4(self, height: List[int]) -> int:
        vol = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                vol += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                vol += right_max - height[right]
        return vol


def test_valid_word_abbreviation():
    s = Solution()
    for height, expected in [
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ]:
        actual = s.trap4(height)
        assert actual == expected, f"{height=} {actual=} {expected=}"
    print("tests passed")

test_valid_word_abbreviation()
