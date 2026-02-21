# Last updated: 2/21/2026, 9:45:21 AM
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets=set()
        for i in range(len(nums)-2):
            first=nums[i]
            j=i+1
            k=len(nums)-1
            while j<k:
                second=nums[j]
                third=nums[k]

                target=first+second+third

                if target>0:
                    k-=1
                elif target<0:
                    j+=1
                
                else:
                    triplets.add((first,second,third))
                    j+=1
                    k-=1
        return triplets
