# Last updated: 2/21/2026, 9:43:52 AM
class Solution:
    
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping1={}
        mapping2={}
        for num in nums1:
            if num not in mapping1:
                mapping1[num]=1
            else:
                mapping1[num]+=1
        
        for num in nums2:
            if num not in mapping2:
                mapping2[num]=1
            else:
                mapping2[num]+=1
        answer=[]
        for k,v in mapping1.items():
            if k in mapping2:
                freq=min(v,mapping2[k])
                while freq>0:
                    answer.append(k)
                    freq-=1
        return answer
           

        

