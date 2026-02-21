# Last updated: 2/21/2026, 9:43:39 AM
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        answer=0
        m=len(flowerbed)
        if n==0:
            return True
        if m<n:
            return False
        if m==1:
            if flowerbed[0]==0:
                n-=1
            if n==0:
                return True
            else:
                return False

        for i in range(len(flowerbed)):
            if flowerbed[i]==0 :
                if ((i>0 and flowerbed[i-1]!=1) and (i<m-1 and flowerbed[i+1]!=1)) or (i==0 and flowerbed[i+1]!=1) or (i==m-1 and flowerbed[i-1]!=1):
                    n-=1
                    flowerbed[i]=1
            if n==0:
                return True
        return False
        