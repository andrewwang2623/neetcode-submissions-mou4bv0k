class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        islands = 0
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if (x, y) in seen:
                    continue
                elif grid[y][x] == '0':
                    continue
                else:
                    islands += 1
                    self.dfs(grid, x, y, seen)
        return islands

    def dfs(self, grid, x, y, seen) -> None:
        #x, y is a island point to begin with
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
            return
        if grid[y][x] == '0':
            return
        if (x, y) in seen:
            return

        seen.add((x, y))

        self.dfs(grid, x-1, y, seen)
        self.dfs(grid, x+1, y, seen)
        self.dfs(grid, x, y-1, seen)
        self.dfs(grid, x, y+1, seen)