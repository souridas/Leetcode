# Last updated: 2/21/2026, 9:45:03 AM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping=dict()
        for i in range(len(strs)):
            s=strs[i]
            temp=dict()
            for c in s:
                if c not in temp:
                    temp[c]=1
                else:
                    temp[c]+=1
            mapping[i]=temp
        answer=[]
        visited = [0]*len(strs)
        for v in mapping.values():
            t1=[]
            for i in range(len(strs)):
                if v==mapping[i] and visited[i]==0:
                    t1.append(strs[i])
                    visited[i]=1
            if t1:
                answer.append(t1)
        return answer

            
