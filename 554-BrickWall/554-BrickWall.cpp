// Last updated: 2/21/2026, 9:43:43 AM
class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
          int n=wall.size();
    unordered_set<int>la;
        int s=0;
        for(int i=0;i<wall[0].size()-1;i++)
        {
            s=s+wall[0][i];
            la.insert(s);
        }
      unordered_map<int,int>chek;
        for(int i=1;i<n;i++)
        {
            int v=0;
            for(int j=0;j<wall[i].size()-1;j++)
            {
                v+=wall[i][j];
                chek[v]++;
            }
        }
        int ans=0;
       for(auto i=chek.begin();i!=chek.end();i++)
       {

           if(la.find(i->first)!=la.end())
           {
               ans=max(ans,1+(i->second));
           }
           else
           {
               ans=max(ans,(i->second));
           }
       }
        if(n==1&& wall[0].size()!=1)
        {
            return 0;
        }
        return n-ans;
    }
};