# Last updated: 2/21/2026, 9:43:45 AM
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0]) 
        dis_mat = [[m*n for i in range(n)] for j in range(m)]
        queue=deque()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        #print('before', dis_mat)
        #print(mat)
        for i in range(m):
            for j in range(n):
                
                if mat[i][j] == 0: 
                    dis_mat[i][j]=0
                    queue.append((i,j))
               
            

        #print('after', dis_mat)
           
        
        while queue:
            curr=queue.popleft()
            i=curr[0]
            j=curr[1]
            
            for dirs in directions:
                n_r=i+dirs[0]
                n_c=j+dirs[1]
              
                if n_r>=0 and n_c>=0 and n_r<m and n_c<n:
                    if dis_mat[n_r][n_c]> 1 + dis_mat[i][j]:
                        dis_mat[n_r][n_c]= 1 + dis_mat[i][j]
                        queue.append((n_r,n_c))
        return dis_mat
        