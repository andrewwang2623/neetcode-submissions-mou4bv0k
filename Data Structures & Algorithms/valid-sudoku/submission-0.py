class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in rows[row]:
                    return False
                if val in cols[col]:
                    return False
                if row < 3:
                    if col < 3:
                        box = 0
                    elif col < 6:
                        box = 1
                    else:
                        box = 2
                elif row < 6:
                    if col < 3:
                        box = 3
                    elif col < 6:
                        box = 4
                    else:
                        box = 5
                else:
                    if col < 3:
                        box = 6
                    elif col < 6:
                        box = 7
                    else:
                        box = 8
                if val in boxes[box]:
                    return False
                rows[row].add(val)
                cols[col].add(val)
                boxes[box].add(val)
        
        return True