class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        for i in strs:
            temp=i
            temp=list(temp)
            temp.sort()
            temp=str(temp)
            if temp in h.keys():
                h[temp].append(i)
            else:
                h[temp]=[]
                h[temp].append(i)
        ans=[]
        for i in h.values():
            ans.append(i)
            # print(h)
        return ans