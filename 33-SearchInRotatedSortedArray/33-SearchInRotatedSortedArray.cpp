// Last updated: 2/21/2026, 9:45:12 AM
class Solution {
public:
    int search(vector<int>& nums, int key) {
        int n=nums.size();
        int l=0,h=n-1;
        while(l<=h)
        {
            int mid=(l+h)/2;
            if(nums[mid]==key)
            {
                return mid;
            }
            if(nums[l]<=nums[mid])
            {
                if(key<=nums[mid] && key>=nums[l])
                {
                    h=mid-1;}
            
                else
                {
                    l=mid+1;
                }
            }
          else 
          {   if(key>=nums[mid] && key<=nums[h])
                {
                    l=mid+1;
                }
               else
               {
                    h=mid-1;
               }
          }
    }
        return -1;
}
};