class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        maxSize = 0
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if (x, y) in seen:
                    continue
                elif grid[y][x] == 0:
                    continue
                else: 
                    size = self.dfs(grid, x, y, seen, 0)
                    if size > maxSize:
                        maxSize = size
        return maxSize

    def dfs(self, grid, x, y, seen, size):
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
            return 0
        if grid[y][x] == 0:
            return 0
        if (x, y) in seen:
            return 0

        seen.add((x, y))
        size += 1

        size += self.dfs(grid, x-1, y, seen, 0)
        size += self.dfs(grid, x+1, y, seen, 0)
        size += self.dfs(grid, x, y-1, seen, 0)
        size += self.dfs(grid, x, y+1, seen, 0)

        return size