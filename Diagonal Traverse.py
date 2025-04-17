class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic = {}
        for i in range(len(mat)): # 0 1 2
            for j in range(len(mat[i])): # 0 1 2 of every i 
                if i + j not in dic:
                    dic[i+j] = []
                dic[i+j].append(mat[i][j])
        res = []
        for k in dic:
            if k %2 == 0:
                dic[k].reverse()
            for i in dic[k]:
                res.append(i)
        return res
            
