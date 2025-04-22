class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        This algorithm transpose the matrix and reverses each row
        """

        for row in range(len(matrix)):
            for col in range(row, len(matrix)):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for i in range(len(matrix)):
            rotated = matrix[i].reverse()
        return rotated
