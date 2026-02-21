# Last updated: 2/21/2026, 9:43:42 AM
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        reshaped_matrix=[]
        num_list=[]
        
        for row in mat:
            for num in row:
                num_list.append(num)

        if r*c == len(num_list):
            for i in range(r):
                reshaped_matrix.append(list([0]*c))
        else:
            return mat
        k=0
        for i in range(r):
            for j in range(c):
                if k<len(num_list):
                    reshaped_matrix[i][j]=num_list[k]
                    k+=1
        return reshaped_matrix