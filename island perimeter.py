"""
Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4


Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.
"""

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]


class Solution(object):
    def islandPerimeter(self, grid):
        m, n = len(grid), len(grid[0])
        land, nei = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    land += 1
                    if i < m - 1 and grid[i + 1][j] == 1:
                        nei += 1
                    if j < n - 1 and grid[i][j + 1] == 1:
                        nei += 1
        return land * 4 - 2 * nei
