class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix = []
        # for row in range(len(matrix)):
            # print(row, matrix[row])
        for i in range(len(matrix[0])):
            new_matrix.append([col[i] for col in matrix])

                

        return new_matrix



        
