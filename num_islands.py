from typing import List 

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    num_islands += 1
                    neighbors = deque([(i, j)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]):
                            continue
                        if grid[row][col] == "0":
                            continue
                        grid[row][col] = "0"
                        for neighbor in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                            neighbors.append(neighbor)

        return num_islands


def test_num_islands():
    s = Solution()
    for case, expected in [
        ([["0"]], 0),
        ([["1"]], 1),
        ([["1", "0"], ["0", "1"]], 2),
    ]: 
        num_islands = s.numIslands(case)
        assert num_islands == expected, f"{num_islands=} {expected=}"

    print("Tests passed")

test_num_islands()
