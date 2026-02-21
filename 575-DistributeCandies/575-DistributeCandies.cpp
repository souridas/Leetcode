// Last updated: 2/21/2026, 9:43:40 AM
class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        int n=candyType.size();
        unordered_set<int> s;
        for(int i=0;i<n;i++)
        {
            s.insert(candyType[i]);
        }
        int m=s.size();
        return min(n/2,m);
    }
};