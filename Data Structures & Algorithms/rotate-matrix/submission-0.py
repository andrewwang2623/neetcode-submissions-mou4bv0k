class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        #transpose
        for i in range(size):
            for j in range(i+1, size):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #reverse rows
        for row in matrix:
            for i in range(size // 2):
                row[i], row[size - 1 - i] = row[size - 1 - i], row[i]
        
        return