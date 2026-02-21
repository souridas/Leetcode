# Last updated: 2/21/2026, 9:43:30 AM
class Solution:
    def fill_util(self,i,j,image,color,val):
        if i<0 or j<0 or i>=len(image) or j>=len(image[0]) or image[i][j]!=val or image[i][j]==color:
            return

        image[i][j]=color
        self.fill_util(i-1,j,image,color,val)
        self.fill_util(i+1,j,image,color,val)
        self.fill_util(i,j-1,image,color,val)
        self.fill_util(i,j+1,image,color,val)
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        val=image[sr][sc]
        self.fill_util(sr,sc,image,color,val)
        return image


        